# Quirks: Traya Health

## Timezones

- **Most timestamp columns are in UTC.** Add 330 minutes (5h30m) for IST conversion.
  - `orders.created_at`, `orders.updated_at`, `orders_v2.delivery_date`, `orders_vw.created_at`, `orders_vw.delivery_date` — all UTC.
  - Use: `date_add('minute', 330, created_at)` for IST conversion in Athena.
- **`activity_date` columns are already in IST.** These are partition keys derived from `created_at`/`createdat` after IST conversion. Do NOT convert them again.
  - Applies to: `engagements.activity_date`, `orders.activity_date`, `google_ads_campaign_hourly.activity_date`, etc.
- **`session_date` in Gupshup tables is IST.** Partition key, no conversion needed.
- **`createdAt_ist` / `sessionStartTime_ist` / `sessionEndTime_ist`** in Gupshup tables are already IST (suffix `_ist`).

## Partition Columns

- **Always filter on partition columns for performance.** Athena scans all data without partition filters.
  - `activity_date` — most tables (STRING, format `YYYY-MM-DD`)
  - `session_date` — Gupshup tables (STRING, format `YYYY-MM-DD`)
  - `yr`, `mon`, `dt` — orders_v2 (INT, INT, DATE)

## Type Casting

- **`order_count` is STRING** in engagements — always `CAST(order_count AS INT)`.
- **`streak_achieve_days` is STRING** in streak_logs — `CAST(streak_achieve_days AS INT)`.
- **`is_credit_transaction`, `is_debit_transaction`, `all_coins_used`** in reward_transactions are STRING — `CAST(... AS BOOLEAN)`.
- **`credit_coins`, `total_debit_coins`** are STRING — `CAST(... AS DOUBLE)`.
- **`is_slot_booked`** in `trayaprod.engagements` is STRING `'True'`/`'False'` — use `CAST(is_slot_booked AS BOOLEAN)` or `= 'True'`.
- **`is_finished`** in `trayaprod.engagements` is STRING `'True'`/`'False'`.

## order_count Reliability

- **`order_count` can disagree with actual order delivery sequence.** For reliable O1/O2/O3 counting, use DENSE_RANK on `orders.delivery_date` instead:
  ```sql
  DENSE_RANK() OVER (PARTITION BY o.case_id ORDER BY o.delivery_date) AS order_number
  ```

## request_type Degradation

- **`request_type` degrades after O1.** 86% of self_service users become empty/no_source at O2+.
- Use O1 engagement's `request_type` as permanent user booking source trait, not later orders.

## Cross-Database Joins

- Athena supports cross-database queries — qualify tables with database name:
  ```sql
  FROM traya_prod_mongo_lz.engagements e
  INNER JOIN tatvav2db_public.orders o ON e.case_id = o.case_id
  ```
- **Bridge table**: `tatvav2db_public.cases` links PostgreSQL world (`case_id` = `cases.id`) to MongoDB world (`user_id` = `cases.user_id`).
- MongoDB tables (`trayaprod.streak_logs`, `trayaprod.app_and_user_details`, `trayaprod.reward_transactions`) use `user_id`, NOT `case_id`. Join via cases table.

## Delivery Status Classification

- Standard filter for "real delivered orders":
  ```sql
  CASE
      WHEN (status = 'void' AND sub_status = 'rto') THEN 'rto'
      WHEN (status = 'void' AND COALESCE(sub_status, '') <> 'rto')
           OR status = 'cancelled' THEN 'cancelled'
      WHEN status IN ('placed', 'shipped', 'processing', 'confirmed',
                      'shipping_pending', 'in_progress') THEN 'in_progress'
      ELSE 'delivered'
  END AS delivery_status
  ```

## Offline Store Exclusion

- Always exclude offline store orders for online analytics:
  ```sql
  WHERE source != 'offline_store'
    AND request_source != 'oms_offline_store'
  ```

## Duplicate Engagement Columns

- `trayaprod.engagements_vw` and `trayaprod.tickets_vw` are the preferred view versions for scorecard pipelines.

## Gender Inconsistency

- `tatvav2db_public.cases.gender` uses `Male`/`Female`
- `tatvav2db_public.users.gender` uses `M`/`F`
- Normalize when joining.

## JSON Parsing

- `engagement_activity_trackings.attempts` requires double JSON parse:
  ```sql
  CROSS JOIN UNNEST(CAST(json_parse(attempts) AS ARRAY(JSON))) AS t(attempt)
  ```
- `orders_vw.order_meta_line_items` — use LIKE for simple variant matching, UNNEST for full expansion.

## Google Ads Account Mapping

- Account IDs are not self-descriptive:
  - `8225036905` = Mool_Health
  - `6970437750` = Clear_Ritual
  - `2853254417` = Main_Female_Account
  - `5963499060` = Main_Male_Account

## PII Protection

- **NEVER expose PII columns in query results or outputs.** The following columns contain personally identifiable information and must not be selected, displayed, or exported:
  - `email`, `phone_number`, `phone`, `chat_phone_number` — from `users_vw`, `ez_traya_users_profile`
  - `first_name`, `last_name`, `name` — from `users_vw`
  - `customerName`, `phone_no` — from `gupshup_v2.chat_data_transformation`
  - Any column containing address details (`order_meta_shipping_address`, `order_meta_billing_address`)
- Use these columns only for JOIN conditions or WHERE filters, never in SELECT output.
- For aggregated reporting, use `case_id` or `user_id` as anonymous identifiers.

## Preferred Mart Tables

- **Order sequence (O1, O2, O3):** Use `traya_marts_ez.ez_traya_int_order_sequence_info` joined on `case_id` and `order_display_id` to get the correct `order_sequence` number. This uses DENSE_RANK excluding void/rto orders — more reliable than raw `order_count`.
  ```sql
  SELECT o.*, seq.order_sequence
  FROM traya_marts_ez.ez_traya_orders_olap o
  LEFT JOIN traya_marts_ez.ez_traya_int_order_sequence_info seq
    ON o.case_id = seq.case_id AND o.order_display_id = seq.order_display_id
  ```
- **Orders OLAP:** `traya_marts_ez.ez_traya_orders_olap` is the single source of truth for all order-related analysis. Contains enriched order data with user demographics, cancellation details, coin redemptions, warehouse, logistics, tracking, pincode data, and `updated_status` (corrects void+rto). Partitioned by `activity_date`.
- **User profiles:** `traya_marts_ez.ez_traya_users_profile` is the canonical user profile table. Contains demographics, form status, order stats, location (zip/state/city), and derived segments (`customer_segment`: lead/new_customer/loyal_customer). One row per user.
- **Tickets:** `traya_marts_ez.ez_traya_tickets` is the enriched ticket mart with comments, history, doctor consultations, call attempts, and CSAT feedback. Prefer this over raw `trayaprod.tickets_vw`.
- **Case summary:** `traya_marts_ez.ez_traya_case_summary` aggregates everything per case — form stats, UTM attribution, scalpie uploads, and order summaries. One row per case. Use for funnel/cohort analysis.
- **Live orders view:** `traya_marts_ez.ez_traya_orders_olap_live_vw` adds `order_sequence` to orders_olap — use when you need both order details and sequence in one table.
