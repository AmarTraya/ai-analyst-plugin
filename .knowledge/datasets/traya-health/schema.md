# Schema: Traya Health

## Aggregated Mart Models (dbt-managed, Hogwarts repo)

| Table | Description |
|-------|-------------|
| `traya_marts_ez.ez_traya_case_summary` | One row per case. Aggregates case attributes, user demographics, form responses, scalpie uploads, UTM attribution, and order statistics. Iceberg table, partitioned by bucket(case_id, 20). |
| `traya_marts_ez.ez_traya_case_summary_vw` | View on ez_traya_case_summary. |
| `traya_marts_ez.ez_traya_orders_olap` | Incremental Iceberg mart for orders OLAP analytics. Enriches orders with user demographics, cancellation details, coin redemptions, warehouse, logistics, tracking, and pincode data. Partitioned by activity_date, merge on order_id. |
| `traya_marts_ez.ez_traya_orders_olap_live_vw` | Live view on ez_traya_orders_olap joined with order sequence info. |
| `traya_marts_ez.ez_traya_tickets` | Incremental Iceberg mart for support tickets. Enriches tickets with comments, history, doctor consultations, call attempts, and CSAT feedback. Merge key: (ticket_id, doctor_consultation_id). |
| `traya_marts_ez.ez_traya_tickets_vw` | View on ez_traya_tickets. |
| `traya_marts_ez.ez_traya_users_profile` | User profile mart combining user demographics, latest form response, age, and order statistics. Partitioned by bucket(case_id, 16). |
| `traya_marts_ez.ez_traya_int_order_sequence_info` | Iceberg table with order sequence per case_id using DENSE_RANK, excluding void/rto orders. Partitioned by bucket(case_id, 16). |
---

## google_analytics.google_ads_adgroup_data_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `customer_id` | varchar | Yes |  |
| `account_name` | varchar(19) | Yes |  |
| `campaign_id` | varchar | Yes |  |
| `campaign_name` | varchar | Yes |  |
| `ad_group_id` | varchar | Yes |  |
| `ad_group_name` | varchar | Yes |  |
| `ad_group_status` | varchar | Yes |  |
| `target_cpa_micros` | bigint | Yes |  |
| `target_cpm_micros` | bigint | Yes |  |
| `target_cpv_micros` | bigint | Yes |  |
| `impressions` | bigint | Yes |  |
| `clicks` | bigint | Yes |  |
| `conversions` | double | Yes |  |
| `cost_inr` | double | Yes |  |
| `ad_network_type` | varchar | Yes |  |
| `ad_sub_network_type` | varchar | Yes |  |
| `campaign_date_ist` | varchar | Yes |  |
| `hour` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## google_analytics.google_ads_campaign_hourly_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `customer_id` | varchar | Yes |  |
| `account_name` | varchar(19) | Yes |  |
| `campaign_id` | varchar | Yes |  |
| `campaign_name` | varchar | Yes |  |
| `impressions` | bigint | Yes |  |
| `clicks` | bigint | Yes |  |
| `cost_inr` | double | Yes |  |
| `ad_network_type` | varchar | Yes |  |
| `ad_sub_network_type` | varchar | Yes |  |
| `campaign_date_ist` | varchar | Yes |  |
| `hour` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.cancelled_orders_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `_hoodie_commit_time` | varchar | Yes |  |
| `cancel_requested_by_user_id` | varchar | Yes |  |
| `cancelled_by_user_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `created_by_user_id` | varchar | Yes |  |
| `id` | varchar | Yes |  |
| `is_cancelled` | varchar | Yes |  |
| `is_lost_damaged` | varchar | Yes |  |
| `is_rto` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `reason` | varchar | Yes |  |
| `refund_applicable` | varchar | Yes |  |
| `refund_transaction_id` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `sub_status` | varchar | Yes |  |
| `sub_status_change_date` | varchar | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `updated_by_user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_activity_log_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `author_id` | varchar | Yes |  |
| `author_name` | varchar | Yes |  |
| `author_email` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `event_id` | varchar | Yes |  |
| `meta` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_assignments_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `role_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_comments_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `comment_text` | varchar | Yes |  |
| `type` | varchar | Yes |  |
| `type_of_comment` | varchar | Yes |  |
| `engagement_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_docs_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `document` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_image_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `image` | varchar | Yes |  |
| `ai_response` | varchar | Yes |  |
| `hair_stage` | varchar | Yes |  |
| `scalpie_type` | varchar | Yes |  |
| `platform` | varchar | Yes |  |
| `screen_location` | varchar | Yes |  |
| `tagged_by` | varchar | Yes |  |
| `tagged_stage` | varchar | Yes |  |
| `is_ai_detected` | boolean | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_referral_codes_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `referral_code` | varchar | Yes |  |
| `device_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_tag_history_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `slug` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.case_tags_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `case_id` | varchar | Yes |  |
| `id` | varchar | Yes |  |
| `tag_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |

## tatvav2db_public.cases_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `assignment_id` | varchar | Yes |  |
| `latest_order_id` | varchar | Yes |  |
| `temporary_assignment_id` | varchar | Yes |  |
| `sales_assignment_id` | varchar | Yes |  |
| `intervention_doctor` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `consult_call_due_date` | timestamp(3) | Yes |  |
| `consult_call_actual_date` | timestamp(3) | Yes |  |
| `last_form_fill_date` | timestamp(3) | Yes |  |
| `latest_order_date` | timestamp(3) | Yes |  |
| `escalated_at` | timestamp(3) | Yes |  |
| `sales_assignment_date` | timestamp(3) | Yes |  |
| `last_answered_call_date` | timestamp(3) | Yes |  |
| `repeat_cart_created_date` | timestamp(3) | Yes |  |
| `status` | varchar | Yes |  |
| `consult_call_tag` | varchar | Yes |  |
| `escalation_status` | varchar | Yes |  |
| `consult_call_version` | varchar | Yes |  |
| `category` | varchar | Yes |  |
| `last_utm_source` | varchar | Yes |  |
| `last_utm_medium` | varchar | Yes |  |
| `last_utm_campaign` | varchar | Yes |  |
| `last_utm_content` | varchar | Yes |  |
| `last_order_source` | varchar | Yes |  |
| `last_answered_call_type` | varchar | Yes |  |
| `tags` | varchar | Yes |  |
| `dnd` | varchar | Yes |  |
| `language` | varchar | Yes |  |
| `communication_channel` | varchar | Yes |  |
| `zoho_customer_id` | varchar | Yes |  |
| `community` | varchar | Yes |  |
| `form_status` | varchar | Yes |  |
| `feedback` | varchar | Yes |  |
| `clinic_id` | varchar | Yes |  |
| `notes` | varchar | Yes |  |
| `latest_order_display_id` | varchar | Yes |  |
| `repeat_cart_link` | varchar | Yes |  |
| `experiment_config` | varchar | Yes |  |
| `consult_call_finished` | boolean | Yes |  |
| `last_order_discount_flag` | boolean | Yes |  |
| `app_user` | boolean | Yes |  |
| `diet_plan_subscription` | boolean | Yes |  |
| `hair_coach_made_cart` | boolean | Yes |  |
| `order_placed_by_hair_coach` | boolean | Yes |  |
| `is_bah_migrated` | boolean | Yes |  |
| `latest_order_count` | integer | Yes |  |
| `unanswered_count` | integer | Yes |  |
| `call_engagement_count` | integer | Yes |  |
| `meta` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.consult_call_feedback_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `feedback` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.consult_slot_bookings_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `slot_id` | varchar | Yes |  |
| `assignment_id` | varchar | Yes |  |
| `booking_time` | timestamp(3) | Yes |  |
| `is_finished` | boolean | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.consumer_subscriptions_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `main_order_id` | varchar | Yes |  |
| `customer_id` | varchar | Yes |  |
| `delivery_frequency` | varchar | Yes |  |
| `payment_frequency` | varchar | Yes |  |
| `duration` | integer | Yes |  |
| `start_date` | date | Yes |  |
| `end_date` | date | Yes |  |
| `store_id` | varchar | Yes |  |
| `shopify_order_id` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `cancelled_by` | varchar | Yes |  |
| `cancelled_at` | timestamp(3) | Yes |  |
| `consent_date` | timestamp(3) | Yes |  |
| `payment_reference_id` | varchar | Yes |  |
| `next_debit_date` | date | Yes |  |
| `cancellation_reason` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `delivery_date` | timestamp(3) | Yes |  |
| `last_paused_cycle_id` | varchar | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.customer_assigned_clinic_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `customer_id` | varchar | Yes |  |
| `clinic_id` | varchar | Yes |  |
| `doctor_id` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |

## tatvav2db_public.customer_computed_data_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `age` | bigint | Yes |  |
| `all_purchased_product_ids` | varchar | Yes |  |
| `app_user_details` | varchar | Yes |  |
| `app_version` | varchar | Yes |  |
| `available_coins` | bigint | Yes |  |
| `case_id` | varchar | Yes |  |
| `chat_phone_number` | varchar | Yes |  |
| `cohort_slug` | varchar | Yes |  |
| `computed_at` | varchar | Yes |  |
| `created_at` | varchar | Yes |  |
| `current_kit` | bigint | Yes |  |
| `current_kit_status` | varchar | Yes |  |
| `current_streak_count` | bigint | Yes |  |
| `current_week_in_kit` | bigint | Yes |  |
| `current_week_start_date` | varchar | Yes |  |
| `customer_type` | varchar | Yes |  |
| `email` | varchar | Yes |  |
| `first_order_date` | varchar | Yes |  |
| `gender` | varchar | Yes |  |
| `in_progress_order_ids` | varchar | Yes |  |
| `is_app_user` | varchar | Yes |  |
| `is_stale` | varchar | Yes |  |
| `kit_expire_days` | bigint | Yes |  |
| `last_answered_call_date` | varchar | Yes |  |
| `last_answered_call_engagement_id` | varchar | Yes |  |
| `last_app_used_at` | varchar | Yes |  |
| `last_called_date` | varchar | Yes |  |
| `last_called_engagement_id` | varchar | Yes |  |
| `last_delivery_date` | varchar | Yes |  |
| `last_log_date` | varchar | Yes |  |
| `last_order_date` | varchar | Yes |  |
| `last_order_delivery_date` | varchar | Yes |  |
| `last_scalpie_uploaded_date` | varchar | Yes |  |
| `last_slot_booking_date` | varchar | Yes |  |
| `last_slot_booking_engagement_id` | varchar | Yes |  |
| `last_streak_date` | varchar | Yes |  |
| `last_ticket_id` | varchar | Yes |  |
| `last_ticket_raised_date` | varchar | Yes |  |
| `latest_order_products` | varchar | Yes |  |
| `lifetime_earned_coins` | bigint | Yes |  |
| `lifetime_spent_coins` | bigint | Yes |  |
| `name` | varchar | Yes |  |
| `nearest_clinic` | varchar | Yes |  |
| `next_kit_update_at` | varchar | Yes |  |
| `next_week_update_at` | varchar | Yes |  |
| `payment_gateway` | varchar | Yes |  |
| `phone_number` | varchar | Yes |  |
| `pincode` | varchar | Yes |  |
| `previous_order_products` | varchar | Yes |  |
| `remaining_kit_count` | bigint | Yes |  |
| `stale_reason` | varchar | Yes |  |
| `total_cancelled_orders` | bigint | Yes |  |
| `total_delivered_orders` | bigint | Yes |  |
| `total_in_progress_orders` | bigint | Yes |  |
| `total_kit_count` | bigint | Yes |  |
| `total_order_count` | bigint | Yes |  |
| `total_rto_orders` | bigint | Yes |  |
| `updated_at` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.customer_visit_logs_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `agent_id` | varchar | Yes |  |
| `customer_id` | varchar | Yes |  |
| `store_id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `name` | varchar | Yes |  |
| `mobile_no` | varchar | Yes |  |
| `gender` | varchar | Yes |  |
| `crm_link` | varchar | Yes |  |
| `summary_of_conversation` | varchar | Yes |  |
| `call_remark` | varchar | Yes |  |
| `call_reminder_remark` | varchar | Yes |  |
| `verbatim_customer_questions` | varchar | Yes |  |
| `source` | varchar | Yes |  |
| `delivery_status` | varchar | Yes |  |
| `placed_order` | boolean | Yes |  |
| `knows_about_traya` | boolean | Yes |  |
| `scalp_test` | boolean | Yes |  |
| `wants_call` | boolean | Yes |  |
| `doc_app_amt` | double | Yes |  |
| `sale_amount` | double | Yes |  |
| `kit_count` | integer | Yes |  |
| `enquiry` | boolean | Yes |  |
| `date` | timestamp(3) | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.delivery_tat_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `pincode` | varchar | Yes |  |
| `origin` | varchar | Yes |  |
| `tat` | integer | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |

## tatvav2db_public.doctor_order_prescriptions_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `prescription` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `version` | integer | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.ez_traya_exploded_orders

Staging view that unions production orders and test orders with normalized types. JSON fields (order_meta) are extracted and casted to native Athena types. Explodes up to 10 line item variants. Used as input to `flat_orders_main` and downstream marts.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes | Order primary key |
| `case_id` | varchar | Yes | Customer case identifier |
| `user_id` | varchar | Yes | User identifier |
| `gender` | varchar | Yes | Gender of the user |
| `order_number` | varchar | Yes | Internal order number |
| `order_display_id` | varchar | Yes | Unique human-readable order display identifier |
| `order_type` | varchar | Yes | Type of order |
| `created_at` | timestamp(3) | Yes | Order creation timestamp (UTC) |
| `updated_at` | timestamp(3) | Yes | Last update timestamp (UTC) |
| `delivery_date` | timestamp(3) | Yes | Delivery date |
| `order_cancelled_date` | timestamp(3) | Yes | Cancellation date |
| `count` | integer | Yes | Order item count |
| `status` | varchar | Yes | Order status (delivered, void, cancelled, etc.) |
| `sub_status` | varchar | Yes | Sub-status (rto, etc.) |
| `is_bulk_order` | boolean | Yes | Bulk order flag |
| `bulk_order_duration` | integer | Yes | Duration of bulk order in months |
| `is_combo` | boolean | Yes | Combo order flag |
| `is_single_order` | boolean | Yes | Single order flag |
| `discount_flag` | boolean | Yes | Whether a discount was applied |
| `discount_code` | varchar | Yes | Applied discount code |
| `coupon_code` | varchar | Yes | Coupon code from order meta discount_applications |
| `discount_amount` | double | Yes | Discount amount |
| `discount_type` | varchar | Yes | Type of discount |
| `utm_source` | varchar | Yes | UTM source tracking |
| `utm_medium` | varchar | Yes | UTM medium tracking |
| `utm_campaign` | varchar | Yes | UTM campaign tracking |
| `utm_content` | varchar | Yes | UTM content tracking |
| `referring_site` | varchar | Yes | Referring site URL |
| `landing_page_url` | varchar | Yes | Landing page URL |
| `source_name` | varchar | Yes | Source name from order meta (web, app) |
| `landing_site` | varchar | Yes | Landing site from order meta |
| `landing_site_ref` | varchar | Yes | Landing site referrer |
| `financial_status` | varchar | Yes | Financial status (paid, pending, refunded) |
| `payment_gateway` | varchar | Yes | Payment gateway used |
| `zip` | varchar | Yes | Shipping address zip/pincode |
| `shipping_city` | varchar | Yes | Shipping address city |
| `default_city` | varchar | Yes | Default city from pincode mapping |
| `country` | varchar | Yes | Shipping address country |
| `province` | varchar | Yes | Shipping address province/state |
| `warehouse_id` | varchar | Yes | Warehouse ID for fulfillment |
| `order_source` | varchar | Yes | Source of the order (app, web, crm, offline_store) |
| `order_rto_update_date` | timestamp(3) | Yes | RTO update date |
| `order_tags` | varchar | Yes | Order tags from meta |
| `order_value` | double | Yes | Total order value (price) |
| `shipping_amount` | double | Yes | Shipping amount charged |
| `total_tax` | double | Yes | Total tax amount |
| `variant_1` | varchar | Yes | Line item variant 1 product name |
| `variant_2` | varchar | Yes | Line item variant 2 product name |
| `variant_3` | varchar | Yes | Line item variant 3 product name |
| `variant_4` | varchar | Yes | Line item variant 4 product name |
| `variant_5` | varchar | Yes | Line item variant 5 product name |
| `variant_6` | varchar | Yes | Line item variant 6 product name |
| `variant_7` | varchar | Yes | Line item variant 7 product name |
| `variant_8` | varchar | Yes | Line item variant 8 product name |
| `variant_9` | varchar | Yes | Line item variant 9 product name |
| `variant_10` | varchar | Yes | Line item variant 10 product name |
| `order_meta` | varchar | Yes | Raw JSON order metadata blob |
| `source_table` | varchar(10) | Yes | Source table indicator (orders or test_orders) |

## tatvav2db_public.ez_traya_int_order_delivery_counts

Incremental Iceberg table maintaining delivery count (del_count) per case_id using DENSE_RANK. Handles rto/void transitions by re-ranking the entire case. Uses S3 checkpoints for incremental processing.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `case_id` | varchar | Yes | Customer case identifier |
| `order_display_id` | varchar | Yes | Unique order display identifier (unique, not null) |
| `del_count` | bigint | Yes | Delivery count — dense rank of order within the case |
| `order_created_at` | timestamp(6) | Yes | Timestamp of order creation |
| `updated_at` | timestamp(6) with time zone | Yes | Timestamp when this row was last computed by dbt |

## tatvav2db_public.ez_traya_int_order_delivery_counts__dbt_tmp

Temporary dbt staging table for ez_traya_int_order_delivery_counts. Same schema — used during incremental merge processing.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `case_id` | varchar | Yes | Customer case identifier |
| `order_display_id` | varchar | Yes | Unique order display identifier |
| `del_count` | bigint | Yes | Delivery count — dense rank of order within the case |
| `order_created_at` | timestamp(6) | Yes | Timestamp of order creation |
| `updated_at` | timestamp(6) with time zone | Yes | Timestamp when this row was last computed by dbt |

## tatvav2db_public.ez_traya_int_order_product_categories

Explodes order line items from JSON, joins to product_sku_mapping and medicine_master, then aggregates product display names by category per order. One row per order_display_id.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `order_display_id` | varchar | Yes | Unique order display identifier (unique, not null) |
| `rx_product` | varchar | Yes | Comma-separated Rx product names |
| `santulan_product` | varchar | Yes | Comma-separated Santulan product names |
| `suppli_product` | varchar | Yes | Comma-separated Supplement product names |
| `topical_product` | varchar | Yes | Comma-separated Topical product names |
| `others` | varchar | Yes | Comma-separated other product names |

## tatvav2db_public.form_responses_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `synthetic_id` | varchar | Yes |  |
| `question` | varchar | Yes |  |
| `question_id` | varchar | Yes |  |
| `response` | varchar | Yes |  |
| `response_id` | varchar | Yes |  |
| `form_id` | varchar | Yes |  |
| `source` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `location_path` | varchar | Yes |  |
| `form_fill_source` | varchar | Yes |  |
| `version` | integer | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.invoices_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `serial_invoice_number` | varchar | Yes |  |
| `invoice_number` | varchar | Yes |  |
| `invoice_date` | timestamp(3) | Yes |  |
| `serial_cn_number` | varchar | Yes |  |
| `cn_number` | varchar | Yes |  |
| `cn_date` | timestamp(3) | Yes |  |
| `order_number` | varchar | Yes |  |
| `order_display_id` | varchar | Yes |  |
| `order_date` | timestamp(3) | Yes |  |
| `fulfillment_status` | varchar | Yes |  |
| `fulfillment_date` | timestamp(3) | Yes |  |
| `warehouse_name` | varchar | Yes |  |
| `delivery_partner` | varchar | Yes |  |
| `courier_partner` | varchar | Yes |  |
| `order_sub_status` | varchar | Yes |  |
| `delivery_date` | timestamp(3) | Yes |  |
| `rto_date` | timestamp(3) | Yes |  |
| `order_status` | varchar | Yes |  |
| `combo_name` | varchar | Yes |  |
| `product_name` | varchar | Yes |  |
| `product_short_name` | varchar | Yes |  |
| `hsn` | varchar | Yes |  |
| `gst_rate` | real | Yes |  |
| `product_quantity` | real | Yes |  |
| `product_price` | real | Yes |  |
| `mrp` | real | Yes |  |
| `discount_perc` | varchar | Yes |  |
| `total_discount` | real | Yes |  |
| `total_gross_value` | real | Yes |  |
| `total_taxable_value` | real | Yes |  |
| `igst` | real | Yes |  |
| `cgst` | real | Yes |  |
| `sgst` | real | Yes |  |
| `total_tax` | real | Yes |  |
| `shipping_charge` | real | Yes |  |
| `shipping_method` | varchar | Yes |  |
| `product_fulfillment_status` | varchar | Yes |  |
| `billing_phone` | varchar | Yes |  |
| `sold_from` | varchar | Yes |  |
| `shipping_province` | varchar | Yes |  |
| `shipped_to_state_code` | varchar | Yes |  |
| `sales_type` | varchar | Yes |  |
| `payment_gateway` | varchar | Yes |  |
| `payment_type` | varchar | Yes |  |
| `payment_transaction_id` | varchar | Yes |  |
| `payment_reconciliation_status` | varchar | Yes |  |
| `payment_reconciliation_id` | varchar | Yes |  |
| `payment_reconciliation_date` | timestamp(3) | Yes |  |
| `actual_payment_recieved` | varchar | Yes |  |
| `gateway_commission` | varchar | Yes |  |
| `gateway_commission_gst` | varchar | Yes |  |
| `refund_date` | timestamp(3) | Yes |  |
| `refund_transaction_id` | varchar | Yes |  |
| `refund_transaction_gateway` | varchar | Yes |  |
| `invoice_source` | varchar | Yes |  |
| `cn_source` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `discount_code` | varchar | Yes |  |
| `email` | varchar | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.medicine_master_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `display_name` | varchar | Yes |  |
| `type` | varchar | Yes |  |
| `group` | varchar | Yes |  |
| `dosage` | varchar | Yes |  |
| `description` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `medicine_slug` | varchar | Yes |  |
| `info` | varchar | Yes |  |
| `is_composition` | boolean | Yes |  |
| `composition` | varchar | Yes |  |
| `medicine_link` | varchar | Yes |  |
| `tax_rate` | decimal(8,2) | Yes |  |
| `detailed_display_name` | varchar | Yes |  |
| `zoho_product_id` | varchar | Yes |  |
| `medicine_short_name` | varchar | Yes |  |
| `medicine_dosage` | varchar | Yes |  |
| `video_link` | varchar | Yes |  |
| `video_banner` | varchar | Yes |  |
| `dosage_code` | varchar | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |

## tatvav2db_public.ndr_actions_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `awb_number` | varchar | Yes |  |
| `cp_code` | varchar | Yes |  |
| `ndr_remark` | varchar | Yes |  |
| `ndr_category` | varchar | Yes |  |
| `ndr_sub_category` | varchar | Yes |  |
| `ndr_time` | timestamp(3) | Yes |  |
| `delivery_attempt` | smallint | Yes |  |
| `ndr_attempt` | smallint | Yes |  |
| `assigned_to` | varchar | Yes |  |
| `assigned_ref_id` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `resolution` | varchar | Yes |  |
| `resolved_at` | timestamp(3) | Yes |  |
| `outcome` | varchar | Yes |  |
| `outcome_at` | timestamp(3) | Yes |  |
| `requested_reattempt_date` | date | Yes |  |
| `reattempt_attempted_at` | date | Yes |  |
| `reattempt_compliant` | boolean | Yes |  |
| `ots_meta` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `activity_date` | date | Yes |  |

## tatvav2db_public.ndr_vendor_requests_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `ndr_action_id` | varchar | Yes |  |
| `vendor` | varchar | Yes |  |
| `category` | varchar | Yes |  |
| `action_type` | varchar | Yes |  |
| `vendor_ref_id` | varchar | Yes |  |
| `request_data` | varchar | Yes |  |
| `response` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `error` | varchar | Yes |  |
| `requested_by_name` | varchar | Yes |  |
| `requested_by_type` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `request_act` | varchar | Yes |  |
| `request_action` | varchar | Yes |  |
| `request_attempts` | varchar | Yes |  |
| `request_awb` | varchar | Yes |  |
| `request_awbnumber` | varchar | Yes |  |
| `request_awb_number` | varchar | Yes |  |
| `request_awb_numbers` | varchar | Yes |  |
| `request_caller` | varchar | Yes |  |
| `request_callstatus` | varchar | Yes |  |
| `request_comments` | varchar | Yes |  |
| `request_conversationminutes` | varchar | Yes |  |
| `request_courier` | varchar | Yes |  |
| `request_cpcode` | varchar | Yes |  |
| `request_deferred_date` | varchar | Yes |  |
| `request_isterminal` | varchar | Yes |  |
| `request_lead_id` | varchar | Yes |  |
| `request_mobile` | varchar | Yes |  |
| `request_ndrrequests` | varchar | Yes |  |
| `request_ndr_action` | varchar | Yes |  |
| `request_outcome` | varchar | Yes |  |
| `request_preferreddate` | varchar | Yes |  |
| `request_reattempt_address_type` | varchar | Yes |  |
| `request_reattempt_date` | varchar | Yes |  |
| `request_reattempt_time` | varchar | Yes |  |
| `request_recordingurl` | varchar | Yes |  |
| `request_responses` | varchar | Yes |  |
| `request_rto_remark` | varchar | Yes |  |
| `request_start_date` | varchar | Yes |  |
| `request_status_update` | varchar | Yes |  |
| `request_teleproject` | varchar | Yes |  |
| `request_waybill` | varchar | Yes |  |
| `activity_date` | date | Yes |  |

## tatvav2db_public.order_doctor_assignments_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `assignment_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.order_history_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `order_status` | varchar | Yes |  |
| `shipping_pending_count` | integer | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.order_warehouses_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `meta` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `warehouse_id` | varchar | Yes |  |
| `allocation_status` | varchar | Yes |  |
| `allocation_status_reason` | varchar | Yes |  |
| `oad_type` | varchar | Yes |  |
| `is_prozo_invoiced` | boolean | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.orders_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `assignment_id` | varchar | Yes |  |
| `order_number` | varchar | Yes |  |
| `order_display_id` | varchar | Yes |  |
| `order_name` | varchar | Yes |  |
| `order_phone_number` | varchar | Yes |  |
| `order_email` | varchar | Yes |  |
| `source` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `tracking_id` | varchar | Yes |  |
| `order_type` | varchar | Yes |  |
| `tracking_url` | varchar | Yes |  |
| `sub_status` | varchar | Yes |  |
| `order_source` | varchar | Yes |  |
| `utm_source` | varchar | Yes |  |
| `utm_medium` | varchar | Yes |  |
| `utm_campaign` | varchar | Yes |  |
| `utm_content` | varchar | Yes |  |
| `landing_page_url` | varchar | Yes |  |
| `discount_code` | varchar | Yes |  |
| `discount_type` | varchar | Yes |  |
| `last_answered_call_type` | varchar | Yes |  |
| `is_location_pending_reason` | varchar | Yes |  |
| `is_invoice_pending_reason` | varchar | Yes |  |
| `is_zoho_failure_reason` | varchar | Yes |  |
| `zoho_sales_order_id` | varchar | Yes |  |
| `zoho_invoice_id` | varchar | Yes |  |
| `zoho_credit_note_id` | varchar | Yes |  |
| `expected_delivery_date` | varchar | Yes |  |
| `order_awb_generating_partner` | varchar | Yes |  |
| `order_shipping_partner` | varchar | Yes |  |
| `order_rto_awb_tracking_link` | varchar | Yes |  |
| `order_rto_awb_no` | varchar | Yes |  |
| `referring_site` | varchar | Yes |  |
| `order_notes` | varchar | Yes |  |
| `shopify_return_id` | varchar | Yes |  |
| `uni_error_reason` | varchar | Yes |  |
| `uni_shipping_code` | varchar | Yes |  |
| `invoice_number` | varchar | Yes |  |
| `credit_note_number` | varchar | Yes |  |
| `clickpost_security_key` | varchar | Yes |  |
| `tracking_company` | varchar | Yes |  |
| `request_source` | varchar | Yes |  |
| `order_reference` | varchar | Yes |  |
| `request_source_sequence` | varchar | Yes |  |
| `internal_order_sequence` | varchar | Yes |  |
| `offline_store` | varchar | Yes |  |
| `delivery_date` | timestamp(3) | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `last_answered_call_date` | timestamp(3) | Yes |  |
| `prozo_assigned_date` | timestamp(3) | Yes |  |
| `order_fulfilled_date` | timestamp(3) | Yes |  |
| `zoho_invoice_date` | timestamp(3) | Yes |  |
| `order_delivery_date` | timestamp(3) | Yes |  |
| `order_cancelled_date` | timestamp(3) | Yes |  |
| `order_rto_update_date` | timestamp(3) | Yes |  |
| `order_return_update_date` | timestamp(3) | Yes |  |
| `order_shipped_date` | timestamp(3) | Yes |  |
| `uni_sales_order_date` | timestamp(3) | Yes |  |
| `uni_fulfillment_date` | timestamp(3) | Yes |  |
| `internal_uni_sales_order_date` | timestamp(3) | Yes |  |
| `count` | integer | Yes |  |
| `bulk_order_duration` | integer | Yes |  |
| `print_count` | integer | Yes |  |
| `call_engagement_count` | integer | Yes |  |
| `zoho_current_status_code` | integer | Yes |  |
| `shopify_refund_return_status_code` | integer | Yes |  |
| `offline_kit_duration` | integer | Yes |  |
| `is_reminder_generated` | boolean | Yes |  |
| `is_bulk_order` | boolean | Yes |  |
| `is_subscription_order` | boolean | Yes |  |
| `notify_prescription_reminder` | boolean | Yes |  |
| `is_single_order` | boolean | Yes |  |
| `is_combo` | boolean | Yes |  |
| `discount_flag` | boolean | Yes |  |
| `is_stock_allocated` | boolean | Yes |  |
| `is_stock_cancelled` | boolean | Yes |  |
| `is_location_pending` | boolean | Yes |  |
| `is_invoice_pending` | boolean | Yes |  |
| `is_zoho_failure` | boolean | Yes |  |
| `is_international` | boolean | Yes |  |
| `lagger` | boolean | Yes |  |
| `uni_invoice_failure` | boolean | Yes |  |
| `uni_cn_failure` | boolean | Yes |  |
| `is_conditioner_free` | boolean | Yes |  |
| `is_offline_order` | boolean | Yes |  |
| `discount_amount` | double | Yes |  |
| `order_meta_id` | varchar | Yes |  |
| `order_meta_admin_graphql_api_id` | varchar | Yes |  |
| `order_meta_app_id` | bigint | Yes |  |
| `order_meta_billing_address` | varchar | Yes |  |
| `order_meta_browser_ip` | varchar | Yes |  |
| `order_meta_buyer_accepts_marketing` | varchar | Yes |  |
| `order_meta_cancel_reason` | varchar | Yes |  |
| `order_meta_cancelled_at` | varchar | Yes |  |
| `order_meta_cart_token` | varchar | Yes |  |
| `order_meta_checkout_id` | bigint | Yes |  |
| `order_meta_checkout_token` | varchar | Yes |  |
| `order_meta_client_details` | varchar | Yes |  |
| `order_meta_closed_at` | varchar | Yes |  |
| `order_meta_company` | varchar | Yes |  |
| `order_meta_confirmation_number` | varchar | Yes |  |
| `order_meta_confirmed` | boolean | Yes |  |
| `order_meta_contact_email` | varchar | Yes |  |
| `order_meta_created_at` | varchar | Yes |  |
| `order_meta_currency` | varchar | Yes |  |
| `order_meta_current_shipping_price_set` | varchar | Yes |  |
| `order_meta_current_subtotal_price` | varchar | Yes |  |
| `order_meta_current_subtotal_price_set` | varchar | Yes |  |
| `order_meta_current_total_additional_fees_set` | varchar | Yes |  |
| `order_meta_current_total_discounts` | varchar | Yes |  |
| `order_meta_current_total_discounts_set` | varchar | Yes |  |
| `order_meta_current_total_duties_set` | varchar | Yes |  |
| `order_meta_current_total_price` | varchar | Yes |  |
| `order_meta_current_total_price_set` | varchar | Yes |  |
| `order_meta_current_total_tax` | varchar | Yes |  |
| `order_meta_current_total_tax_set` | varchar | Yes |  |
| `order_meta_customer` | varchar | Yes |  |
| `order_meta_customer_locale` | varchar | Yes |  |
| `order_meta_device_id` | varchar | Yes |  |
| `order_meta_discount_applications` | varchar | Yes |  |
| `order_meta_discount_codes` | varchar | Yes |  |
| `order_meta_duties_included` | boolean | Yes |  |
| `order_meta_email` | varchar | Yes |  |
| `order_meta_estimated_taxes` | boolean | Yes |  |
| `order_meta_financial_status` | varchar | Yes |  |
| `order_meta_fulfillment_status` | varchar | Yes |  |
| `order_meta_fulfillments` | varchar | Yes |  |
| `order_meta_gateway` | varchar | Yes |  |
| `order_meta_internal_sequence` | varchar | Yes |  |
| `order_meta_landing_site` | varchar | Yes |  |
| `order_meta_landing_site_ref` | varchar | Yes |  |
| `order_meta_line_item_groups` | varchar | Yes |  |
| `order_meta_line_items` | varchar | Yes |  |
| `order_meta_location_id` | bigint | Yes |  |
| `order_meta_mainorderid` | varchar | Yes |  |
| `order_meta_mainstatus` | varchar | Yes |  |
| `order_meta_mainsubstatus` | varchar | Yes |  |
| `order_meta_merchant_business_entity_id` | varchar | Yes |  |
| `order_meta_merchant_of_record_app_id` | varchar | Yes |  |
| `order_meta_meta` | varchar | Yes |  |
| `order_meta_name` | varchar | Yes |  |
| `order_meta_note` | varchar | Yes |  |
| `order_meta_note_attributes` | varchar | Yes |  |
| `order_meta_number` | bigint | Yes |  |
| `order_meta_order_number` | varchar | Yes |  |
| `order_meta_order_reference` | varchar | Yes |  |
| `order_meta_order_status_url` | varchar | Yes |  |
| `order_meta_original_line_items` | varchar | Yes |  |
| `order_meta_original_total_additional_fees_set` | varchar | Yes |  |
| `order_meta_original_total_duties_set` | varchar | Yes |  |
| `order_meta_payment_details` | varchar | Yes |  |
| `order_meta_payment_gateway_names` | varchar | Yes |  |
| `order_meta_payment_terms` | varchar | Yes |  |
| `order_meta_phone` | varchar | Yes |  |
| `order_meta_po_number` | varchar | Yes |  |
| `order_meta_presentment_currency` | varchar | Yes |  |
| `order_meta_processed_at` | varchar | Yes |  |
| `order_meta_processing_method` | varchar | Yes |  |
| `order_meta_reference` | varchar | Yes |  |
| `order_meta_referring_site` | varchar | Yes |  |
| `order_meta_refunds` | varchar | Yes |  |
| `order_meta_request_source` | varchar | Yes |  |
| `order_meta_request_source_sequence` | varchar | Yes |  |
| `order_meta_returns` | varchar | Yes |  |
| `order_meta_shipping_address` | varchar | Yes |  |
| `order_meta_shipping_lines` | varchar | Yes |  |
| `order_meta_shopflo_order_id` | varchar | Yes |  |
| `order_meta_source_identifier` | varchar | Yes |  |
| `order_meta_source_name` | varchar | Yes |  |
| `order_meta_source_url` | varchar | Yes |  |
| `order_meta_subtotal_price` | varchar | Yes |  |
| `order_meta_subtotal_price_set` | varchar | Yes |  |
| `order_meta_tags` | varchar | Yes |  |
| `order_meta_tax_exempt` | boolean | Yes |  |
| `order_meta_tax_lines` | varchar | Yes |  |
| `order_meta_taxes_included` | boolean | Yes |  |
| `order_meta_test` | varchar | Yes |  |
| `order_meta_token` | varchar | Yes |  |
| `order_meta_total_cash_rounding_payment_adjustment_set` | varchar | Yes |  |
| `order_meta_total_cash_rounding_refund_adjustment_set` | varchar | Yes |  |
| `order_meta_total_discounts` | varchar | Yes |  |
| `order_meta_total_discounts_set` | varchar | Yes |  |
| `order_meta_total_line_items_price` | varchar | Yes |  |
| `order_meta_total_line_items_price_set` | varchar | Yes |  |
| `order_meta_total_outstanding` | varchar | Yes |  |
| `order_meta_total_price` | varchar | Yes |  |
| `order_meta_total_price_set` | varchar | Yes |  |
| `order_meta_total_price_usd` | varchar | Yes |  |
| `order_meta_total_shipping_price_set` | varchar | Yes |  |
| `order_meta_total_tax` | varchar | Yes |  |
| `order_meta_total_tax_set` | varchar | Yes |  |
| `order_meta_total_tip_received` | varchar | Yes |  |
| `order_meta_total_weight` | bigint | Yes |  |
| `order_meta_transaction` | varchar | Yes |  |
| `order_meta_updated_at` | varchar | Yes |  |
| `order_meta_user_id` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.post_purchase_feedback_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `agent_id` | varchar | Yes |  |
| `app_usage` | boolean | Yes |  |
| `ivr_number_saved` | boolean | Yes |  |
| `review_on_google` | boolean | Yes |  |
| `kit_marking_explained` | boolean | Yes |  |
| `travelling_guidance_explained` | boolean | Yes |  |
| `book_a_slot_explained` | boolean | Yes |  |
| `follow_up_call_explained` | boolean | Yes |  |
| `reason_if_not_booked` | varchar | Yes |  |
| `customer_preferred_slot` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.product_sku_mapping_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `medicine_id` | varchar | Yes |  |
| `source` | varchar | Yes |  |
| `product_id` | varchar | Yes |  |
| `is_direct_shipping` | boolean | Yes |  |
| `product_principal_id` | varchar | Yes |  |
| `product_price` | decimal(8,2) | Yes |  |
| `is_combo` | boolean | Yes |  |
| `combo_items` | varchar | Yes |  |
| `image_cdn_path` | varchar | Yes |  |
| `cart_cdn_images` | varchar | Yes |  |
| `mobile_image_path` | varchar | Yes |  |
| `web_mobile_screen_images` | varchar | Yes |  |
| `web_male_mobile` | varchar | Yes |  |
| `sku_styled_image` | varchar | Yes |  |
| `sku_hinglish_image` | varchar | Yes |  |
| `single_images` | varchar | Yes |  |
| `single_half_images` | varchar | Yes |  |
| `sale_theme_male_images` | varchar | Yes |  |
| `sale_theme_female_images` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.referral_discounts_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `referring_case_id` | varchar | Yes |  |
| `discount_code` | varchar | Yes |  |
| `discount_value` | integer | Yes |  |
| `discount_type` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `min_order_value` | integer | Yes |  |
| `source` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.roles_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `name` | varchar | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |

## tatvav2db_public.settings_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `key` | varchar | Yes |  |
| `value` | varchar | Yes |  |
| `is_visible` | boolean | Yes |  |
| `is_editable` | boolean | Yes |  |
| `description` | varchar | Yes |  |
| `userid` | varchar | Yes |  |
| `first_name` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.slots_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `slot_time` | timestamp(3) | Yes |  |
| `level` | varchar | Yes |  |
| `role_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.subscription_cycles_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `subscription_id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `payment_reference_id` | varchar | Yes |  |
| `meta` | varchar | Yes |  |
| `start_date` | timestamp(3) | Yes |  |
| `end_date` | timestamp(3) | Yes |  |
| `billed_at` | timestamp(3) | Yes |  |
| `payment_status` | varchar | Yes |  |
| `retries` | integer | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.subscription_transactions_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `subscription_cycle_id` | varchar | Yes |  |
| `subscription_id` | varchar | Yes |  |
| `customer_id` | varchar | Yes |  |
| `event_type` | varchar | Yes |  |
| `amount` | decimal(10,2) | Yes |  |
| `currency` | varchar | Yes |  |
| `transaction_status` | varchar | Yes |  |
| `transaction_reference` | varchar | Yes |  |
| `card_number` | varchar | Yes |  |
| `card_type` | varchar | Yes |  |
| `request_body` | varchar | Yes |  |
| `response_body` | varchar | Yes |  |
| `transaction_time_stamp` | timestamp(3) | Yes |  |
| `order_id` | varchar | Yes |  |
| `payment_mode` | varchar | Yes |  |
| `transaction_channel` | varchar | Yes |  |
| `device_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.tag_master_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `community_check` | varchar | Yes |  |
| `display_name` | varchar | Yes |  |
| `id` | varchar | Yes |  |
| `slug` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |

## tatvav2db_public.user_call_provider_mapping_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `provider_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `external_agent_id` | varchar | Yes |  |
| `next_call` | boolean | Yes |  |
| `is_active` | boolean | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.user_devices_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `device_token` | varchar | Yes |  |
| `platform` | varchar | Yes |  |
| `provider` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.user_doctor_type_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `doctor_id` | varchar | Yes |  |
| `type` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.user_groups_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `group_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.user_language_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `known_language` | varchar | Yes |  |
| `preferred_language` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.user_notification_preferences_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `sms_disabled` | boolean | Yes |  |
| `email_disabled` | boolean | Yes |  |
| `push_disabled` | boolean | Yes |  |
| `waba_disabled` | boolean | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |

## tatvav2db_public.users_roles_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `role_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.users_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `doj` | timestamp(3) | Yes |  |
| `ojt_start_date` | timestamp(3) | Yes |  |
| `ojt_end_date` | timestamp(3) | Yes |  |
| `production_start_date` | timestamp(3) | Yes |  |
| `relieved_date` | timestamp(3) | Yes |  |
| `email` | varchar | Yes |  |
| `phone_number` | varchar | Yes |  |
| `first_name` | varchar | Yes |  |
| `last_name` | varchar | Yes |  |
| `encrypted_password` | varchar | Yes |  |
| `gender` | varchar | Yes |  |
| `shopify_customer_id` | varchar | Yes |  |
| `alternate_phone` | varchar | Yes |  |
| `alternate_email` | varchar | Yes |  |
| `calendly_link` | varchar | Yes |  |
| `diet_plan_link` | varchar | Yes |  |
| `profile_pic` | varchar | Yes |  |
| `chat_phone_number` | varchar | Yes |  |
| `restore_id` | varchar | Yes |  |
| `external_id` | varchar | Yes |  |
| `house` | varchar | Yes |  |
| `location` | varchar | Yes |  |
| `process` | varchar | Yes |  |
| `team` | varchar | Yes |  |
| `call_provider` | varchar | Yes |  |
| `reporting_manager` | varchar | Yes |  |
| `desgination` | varchar | Yes |  |
| `shift` | varchar | Yes |  |
| `week_off` | varchar | Yes |  |
| `current_status` | varchar | Yes |  |
| `employee_id` | varchar | Yes |  |
| `sub_process` | varchar | Yes |  |
| `batch_number` | varchar | Yes |  |
| `certified` | varchar | Yes |  |
| `meta` | varchar | Yes |  |
| `v1_case_id` | integer | Yes |  |
| `level` | integer | Yes |  |
| `voitekk_id` | integer | Yes |  |
| `is_active` | boolean | Yes |  |
| `deactivated` | boolean | Yes |  |
| `is_consult_doctor` | boolean | Yes |  |
| `is_consult_doctor_active` | boolean | Yes |  |
| `can_do_female_presc` | boolean | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.warehouse_skus_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `sku_id` | varchar | Yes |  |
| `warehouse_id` | varchar | Yes |  |
| `available` | integer | Yes |  |
| `on_hold` | integer | Yes |  |
| `buffer` | integer | Yes |  |
| `reject` | integer | Yes |  |
| `rto` | integer | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.warehouses_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `provider` | varchar | Yes |  |
| `name` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `is_valid_warehouse` | boolean | Yes |  |
| `code` | varchar | Yes |  |
| `meta` | varchar | Yes |  |
| `main_warehouse_id` | varchar | Yes |  |
| `zoho_warehouse_id` | varchar | Yes |  |
| `zoho_branch_id` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## tatvav2db_public.zero_value_orders_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `previous_order_id` | varchar | Yes |  |
| `original_price` | double | Yes |  |
| `category` | varchar | Yes |  |
| `order_placer_email` | varchar | Yes |  |
| `order_placer_name` | varchar | Yes |  |
| `order_placer_id` | varchar | Yes |  |
| `reason` | varchar | Yes |  |
| `created_at` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## traya_marts_ez.ez_traya_active_customer_base

Pre-aggregated active customer base snapshot. Groups customers by period, gender, zip, and order bucket for quick cohort sizing. Refreshed periodically with `run_ts_ist` indicating when each snapshot was computed.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `run_ts_ist` | timestamp(6) | Yes | Timestamp when this snapshot was computed (IST) |
| `period` | varchar | Yes | Time period label for the snapshot (e.g., monthly, weekly) |
| `gender` | varchar | Yes | Gender bucket (Male, Female) |
| `zip` | varchar | Yes | Shipping zip/pincode bucket |
| `order_bucket` | varchar | Yes | Order count bucket for segmentation (e.g., 1-3, 4+) |
| `unique_case_ids` | bigint | Yes | Count of distinct active case_ids in this segment |

## traya_marts_ez.ez_traya_case_summary

One row per case. Aggregates case attributes, user demographics, form responses, scalpie uploads, UTM attribution, and order statistics. Partitioned by bucket(case_id, 20). Iceberg table.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `case_id` | varchar | Yes | Unique case identifier (primary key, one row per case) |
| `lead_date` | timestamp(6) | Yes | Case creation timestamp converted to IST (UTC+5:30) |
| `user_id` | varchar | Yes | User identifier linked to this case |
| `app_user` | boolean | Yes | Whether the user is an app user |
| `language` | varchar | Yes | Language preference of the user |
| `gender` | varchar | Yes | Gender of the user |
| `first_name` | varchar | Yes | First name of the user |
| `community` | varchar | Yes | Community tag display name from tag_master (community_check=true) |
| `total_scalpie_upload` | bigint | Yes | Total number of distinct scalpie images uploaded for this case |
| `first_scalpie_upload_timestamp` | timestamp(6) | Yes | Timestamp of the earliest scalpie image upload (IST) |
| `latest_scalpie_upload_timestamp` | timestamp(6) | Yes | Timestamp of the most recent scalpie image upload (IST) |
| `total_form_start` | bigint | Yes | Count of distinct form submissions started (pre-first-order forms only) |
| `total_form_complete` | bigint | Yes | Count of distinct form submissions completed with status=filled (pre-first-order only) |
| `first_form_start_ts_ist` | timestamp(6) | Yes | Timestamp when the earliest pre-order form was started (IST) |
| `latest_form_start_ts_ist` | timestamp(6) | Yes | Timestamp when the most recent pre-order form was started (IST) |
| `first_form_complete_at_ist` | timestamp(6) | Yes | Timestamp when the earliest pre-order form was completed (IST) |
| `latest_form_complete_at_ist` | timestamp(6) | Yes | Timestamp when the most recent pre-order form was completed (IST) |
| `first_synthetic_id` | varchar | Yes | Synthetic ID of the earliest pre-order form submission |
| `first_form_fill_source` | varchar | Yes | Source channel of the first form fill (e.g., app, web) |
| `first_location_path` | varchar | Yes | Location path of the first form submission |
| `first_utm_source` | varchar | Yes | UTM source from the earliest form response ever (unfiltered by order date) |
| `first_utm_medium` | varchar | Yes | UTM medium from the earliest form response ever (unfiltered by order date) |
| `first_utm_campaign` | varchar | Yes | UTM campaign from the earliest form response ever (unfiltered by order date) |
| `active_synthetic_id` | varchar | Yes | Synthetic ID of the latest/active pre-order form submission |
| `latest_form_fill_source` | varchar | Yes | Source channel of the latest pre-order form fill |
| `latest_form_status` | varchar | Yes | Status of the latest pre-order form (e.g., filled, started) |
| `latest_location_path` | varchar | Yes | Location path of the latest pre-order form submission |
| `age` | varchar | Yes | User age from the most recent C1d form response (unfiltered) |
| `latest_utm_source` | varchar | Yes | UTM source from the most recent form response ever (unfiltered) |
| `latest_utm_medium` | varchar | Yes | UTM medium from the most recent form response ever (unfiltered) |
| `latest_utm_campaign` | varchar | Yes | UTM campaign from the most recent form response ever (unfiltered) |
| `stage` | varchar | Yes | Hair loss stage from latest form response (COALESCE of question IDs: 2e, hairLossStage, hair_vol1, 4f) |
| `first_order_date` | timestamp(6) | Yes | Timestamp of the first order placed by this case (IST) |
| `latest_order_date` | timestamp(6) | Yes | Timestamp of the most recent order placed by this case (IST) |
| `first_delivery_date` | timestamp(6) | Yes | Earliest delivery date across all orders for this case |
| `latest_delivery_date` | timestamp(6) | Yes | Most recent delivery date across all orders for this case |
| `total_orders` | bigint | Yes | Total number of distinct orders for this case |
| `total_cancelled_orders` | bigint | Yes | Count of void orders with cancel_status=cancelled |
| `total_rto_orders` | bigint | Yes | Count of void orders with cancel_status=rto |
| `total_delivered_orders` | bigint | Yes | Count of orders with status=delivered |
| `total_bulk_orders` | bigint | Yes | Count of bulk orders (is_bulk_order=true) |
| `total_kit_orders` | bigint | Yes | Count of kit orders (is_single_order=false) |
| `total_app_orders` | bigint | Yes | Count of orders from app source (order_source LIKE '%app%') |
| `total_crm_orders` | bigint | Yes | Count of orders from CRM source |
| `total_offline_orders` | bigint | Yes | Count of orders from offline stores |
| `total_web_orders` | bigint | Yes | Count of web orders (non-app, non-CRM, non-offline) |
| `first_order_display_id` | varchar | Yes | Display ID of the chronologically first order |
| `latest_order_display_id` | varchar | Yes | Display ID of the chronologically latest order |
| `first_order_source` | varchar | Yes | Source channel of the first order |
| `latest_order_source` | varchar | Yes | Source channel of the latest order |
| `first_non_void_order_display_id` | varchar | Yes | Display ID of the first non-void order |
| `first_non_void_order_date` | timestamp(6) | Yes | Timestamp of the first non-void order (IST) |
| `latest_non_void_order_display_id` | varchar | Yes | Display ID of the latest non-void order |
| `latest_non_void_order_date` | timestamp(6) | Yes | Timestamp of the latest non-void order (IST) |
| `aud_created_at` | timestamp(6) with time zone | Yes | Audit timestamp when this row was created by dbt |
| `aud_updated_at` | timestamp(6) with time zone | Yes | Audit timestamp when this row was last written by dbt |

## traya_marts_ez.ez_traya_case_summary_vw

View on ez_traya_case_summary. One row per case. Same schema and semantics as the base Iceberg table.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `case_id` | varchar | Yes | Unique case identifier (primary key, one row per case) |
| `lead_date` | timestamp(3) | Yes | Case creation timestamp converted to IST (UTC+5:30) |
| `user_id` | varchar | Yes | User identifier linked to this case |
| `app_user` | boolean | Yes | Whether the user is an app user |
| `language` | varchar | Yes | Language preference of the user |
| `gender` | varchar | Yes | Gender of the user |
| `first_name` | varchar | Yes | First name of the user |
| `community` | varchar | Yes | Community tag display name from tag_master (community_check=true) |
| `total_scalpie_upload` | bigint | Yes | Total number of distinct scalpie images uploaded for this case |
| `first_scalpie_upload_timestamp` | timestamp(3) | Yes | Timestamp of the earliest scalpie image upload (IST) |
| `latest_scalpie_upload_timestamp` | timestamp(3) | Yes | Timestamp of the most recent scalpie image upload (IST) |
| `total_form_start` | bigint | Yes | Count of distinct form submissions started (pre-first-order forms only) |
| `total_form_complete` | bigint | Yes | Count of distinct form submissions completed with status=filled (pre-first-order only) |
| `first_form_start_ts_ist` | timestamp(3) | Yes | Timestamp when the earliest pre-order form was started (IST) |
| `latest_form_start_ts_ist` | timestamp(3) | Yes | Timestamp when the most recent pre-order form was started (IST) |
| `first_form_complete_at_ist` | timestamp(3) | Yes | Timestamp when the earliest pre-order form was completed (IST) |
| `latest_form_complete_at_ist` | timestamp(3) | Yes | Timestamp when the most recent pre-order form was completed (IST) |
| `first_synthetic_id` | varchar | Yes | Synthetic ID of the earliest pre-order form submission |
| `first_form_fill_source` | varchar | Yes | Source channel of the first form fill (e.g., app, web) |
| `first_location_path` | varchar | Yes | Location path of the first form submission |
| `first_utm_source` | varchar | Yes | UTM source from the earliest form response ever (unfiltered by order date) |
| `first_utm_medium` | varchar | Yes | UTM medium from the earliest form response ever (unfiltered by order date) |
| `first_utm_campaign` | varchar | Yes | UTM campaign from the earliest form response ever (unfiltered by order date) |
| `active_synthetic_id` | varchar | Yes | Synthetic ID of the latest/active pre-order form submission |
| `latest_form_fill_source` | varchar | Yes | Source channel of the latest pre-order form fill |
| `latest_form_status` | varchar | Yes | Status of the latest pre-order form (e.g., filled, started) |
| `latest_location_path` | varchar | Yes | Location path of the latest pre-order form submission |
| `age` | varchar | Yes | User age from the most recent C1d form response (unfiltered) |
| `latest_utm_source` | varchar | Yes | UTM source from the most recent form response ever (unfiltered) |
| `latest_utm_medium` | varchar | Yes | UTM medium from the most recent form response ever (unfiltered) |
| `latest_utm_campaign` | varchar | Yes | UTM campaign from the most recent form response ever (unfiltered) |
| `stage` | varchar | Yes | Hair loss stage from latest form response (COALESCE of question IDs: 2e, hairLossStage, hair_vol1, 4f) |
| `first_order_date` | timestamp(3) | Yes | Timestamp of the first order placed by this case (IST) |
| `latest_order_date` | timestamp(3) | Yes | Timestamp of the most recent order placed by this case (IST) |
| `first_delivery_date` | timestamp(3) | Yes | Earliest delivery date across all orders for this case |
| `latest_delivery_date` | timestamp(3) | Yes | Most recent delivery date across all orders for this case |
| `total_orders` | bigint | Yes | Total number of distinct orders for this case |
| `total_cancelled_orders` | bigint | Yes | Count of void orders with cancel_status=cancelled |
| `total_rto_orders` | bigint | Yes | Count of void orders with cancel_status=rto |
| `total_delivered_orders` | bigint | Yes | Count of orders with status=delivered |
| `total_bulk_orders` | bigint | Yes | Count of bulk orders (is_bulk_order=true) |
| `total_kit_orders` | bigint | Yes | Count of kit orders (is_single_order=false) |
| `total_app_orders` | bigint | Yes | Count of orders from app source (order_source LIKE '%app%') |
| `total_crm_orders` | bigint | Yes | Count of orders from CRM source |
| `total_offline_orders` | bigint | Yes | Count of orders from offline stores |
| `total_web_orders` | bigint | Yes | Count of web orders (non-app, non-CRM, non-offline) |
| `first_order_display_id` | varchar | Yes | Display ID of the chronologically first order |
| `latest_order_display_id` | varchar | Yes | Display ID of the chronologically latest order |
| `first_order_source` | varchar | Yes | Source channel of the first order |
| `latest_order_source` | varchar | Yes | Source channel of the latest order |
| `first_non_void_order_display_id` | varchar | Yes | Display ID of the first non-void order |
| `first_non_void_order_date` | timestamp(3) | Yes | Timestamp of the first non-void order (IST) |
| `latest_non_void_order_display_id` | varchar | Yes | Display ID of the latest non-void order |
| `latest_non_void_order_date` | timestamp(3) | Yes | Timestamp of the latest non-void order (IST) |
| `aud_created_at` | timestamp(3) | Yes | Audit timestamp when this row was created by dbt |
| `aud_updated_at` | timestamp(3) | Yes | Audit timestamp when this row was last written by dbt |

## traya_marts_ez.ez_traya_int_order_sequence_info

Order sequence per case using DENSE_RANK over created_at, excluding void and rto orders. Use this to get the correct O1/O2/O3 numbering — join on `case_id` + `order_display_id`. Iceberg table, partitioned by bucket(case_id, 16).

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `case_id` | varchar | Yes | Customer case identifier or we can say unique identifier for customer |
| `order_display_id` | varchar | Yes | Unique order display identifier |
| `order_created_at` | timestamp(6) | Yes | Timestamp of order creation |
| `order_sequence` | bigint | Yes | Dense rank of order within the case (excludes void/rto) |
| `updated_at` | timestamp(6) with time zone | Yes | Timestamp when this row was last computed |

## traya_marts_ez.ez_traya_orders_olap

Single source of truth for all order-related analysis. Incremental Iceberg mart enriching orders with user demographics, cancellation details (updated_status corrects void+rto), coin redemptions, warehouse, logistics, tracking, and pincode data. Partitioned by activity_date, merge on order_id. Join with `ez_traya_int_order_sequence_info` on `case_id` + `order_display_id` for O1/O2/O3 sequence.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `order_id` | varchar | Yes | Order primary key (orders.id) |
| `case_id` | varchar | Yes | Customer case identifier |
| `user_id` | varchar | Yes | User identifier |
| `order_number` | varchar | Yes | Shopify order number |
| `order_display_id` | varchar | Yes | Unique human-readable order display identifier |
| `order_type` | varchar | Yes | Type of order |
| `order_created_at` | timestamp(6) | Yes | Timestamp when the order was created |
| `order_updated_at` | timestamp(6) | Yes | Timestamp when the order was last updated |
| `order_delivery_at` | timestamp(6) | Yes | Delivery date of the order |
| `order_cancelled_at` | timestamp(6) | Yes | Timestamp when the order was cancelled (if applicable) |
| `order_count` | integer | Yes | Order count field from the orders table |
| `status` | varchar | Yes | Current order status (e.g., delivered, void, rto) |
| `sub_status` | varchar | Yes | Order sub-status |
| `updated_status` | varchar | Yes | Status updated with RTO from cancelled_orders (rto if cancel_status is rto, else original status) |
| `uni_sales_order_date_ts` | timestamp(6) | Yes | Unicommerce sales order date |
| `uni_fulfillment_date_ts` | timestamp(6) | Yes | Unicommerce fulfillment date |
| `uni_shipping_code` | varchar | Yes | Unicommerce shipping code |
| `offline_store` | varchar | Yes | Offline store identifier (if applicable) |
| `is_bulk_order` | boolean | Yes | Whether this is a bulk order |
| `bulk_order_duration` | integer | Yes | Duration of bulk order in months |
| `is_combo` | boolean | Yes | Whether this is a combo order |
| `is_subscription_order` | boolean | Yes | Whether this is a subscription order |
| `is_international` | boolean | Yes | Whether this is an international order |
| `is_conditioner_free` | boolean | Yes | Whether conditioner was free with this order |
| `is_single_order` | boolean | Yes | Whether this is a single order |
| `discount_flag` | boolean | Yes | Whether a discount was applied |
| `is_offline_order` | boolean | Yes | Whether this is an offline order |
| `discount_code` | varchar | Yes | Discount code applied to the order |
| `coupon_code` | varchar | Yes | Coupon code extracted from order meta discount_applications |
| `utm_source` | varchar | Yes | UTM source tracking parameter |
| `utm_medium` | varchar | Yes | UTM medium tracking parameter |
| `utm_campaign` | varchar | Yes | UTM campaign tracking parameter |
| `referring_site` | varchar | Yes | Referring site URL |
| `landing_page_url` | varchar | Yes | Landing page URL for the order |
| `clinic_id` | varchar | Yes | Clinic identifier extracted from order meta note_attributes |
| `clinic_name` | varchar | Yes | Clinic name extracted from order meta note_attributes |
| `courier` | varchar | Yes | Tracking/courier company name |
| `tracking_id` | varchar | Yes | Shipment tracking ID |
| `tracking_url` | varchar | Yes | Shipment tracking URL |
| `order_meta_source_name` | varchar | Yes | Source name from order meta (e.g., web, app) |
| `order_meta_landing_site` | varchar | Yes | Landing site from order meta |
| `order_meta_landing_site_ref` | varchar | Yes | Landing site referrer from order meta |
| `order_meta_financial_status` | varchar | Yes | Financial status from order meta (e.g., paid, pending) |
| `gender` | varchar | Yes | Gender of the user |
| `user_created_at` | timestamp(6) | Yes | Timestamp when the user account was created |
| `is_lost_damaged` | boolean | Yes | Whether the order was lost or damaged |
| `refund_applicable` | boolean | Yes | Whether a refund is applicable for the cancelled order |
| `total_discount_amount` | double | Yes | Total discount amount applied to the order |
| `discount_type` | varchar | Yes | Type of discount applied |
| `coins_discount_amount` | double | Yes | Amount redeemed via Traya coins/rewards |
| `payment_gateway` | varchar | Yes | Payment gateway used for the order |
| `order_source` | varchar | Yes | Source of the order |
| `order_meta_tags` | varchar | Yes | Tags from order meta |
| `order_value` | double | Yes | Total order value (price) |
| `shipping_amount` | double | Yes | Shipping amount charged |
| `total_tax` | double | Yes | Total tax amount |
| `picked_up_at` | timestamp(6) | Yes | Timestamp when the shipment was picked up |
| `first_out_for_delivery_at` | timestamp(6) | Yes | Timestamp of first out-for-delivery attempt |
| `total_delivery_attempts` | integer | Yes | Total number of delivery attempts |
| `warehouse` | varchar | Yes | Warehouse name from which the order was fulfilled |
| `cp_code` | varchar | Yes | Courier partner code from order tracking |
| `sub_cp` | varchar | Yes | Sub courier partner from order tracking |
| `delivery_city` | varchar | Yes | Delivery city derived from pincode master |
| `zip` | varchar | Yes | Shipping address zip/pincode |
| `shipping_city` | varchar | Yes | Shipping address city |
| `country` | varchar | Yes | Shipping address country |
| `province` | varchar | Yes | Shipping address province/state |
| `delivery_promise_date_customer` | timestamp(6) | Yes | Estimated delivery date based on order creation + pincode TAT |
| `mark_date` | date | Yes | Date when the order was marked as cancelled/RTO |
| `activity_date` | varchar | Yes | Activity date partition column (string format) |
| `aud_updated_at` | timestamp(6) with time zone | Yes | Audit timestamp when this row was last written by dbt (IST) |

## traya_marts_ez.ez_traya_orders_olap_live_vw

Live view on ez_traya_orders_olap joined with order sequence info. Same semantics as the base Iceberg table with an additional order_sequence column.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `order_id` | varchar | Yes | Order primary key (orders.id) |
| `case_id` | varchar | Yes | Customer case identifier |
| `user_id` | varchar | Yes | User identifier |
| `order_number` | varchar | Yes | Shopify order number |
| `order_display_id` | varchar | Yes | Unique human-readable order display identifier |
| `order_type` | varchar | Yes | Type of order |
| `order_created_at` | timestamp(3) | Yes | Timestamp when the order was created |
| `order_updated_at` | timestamp(3) | Yes | Timestamp when the order was last updated |
| `order_delivery_at` | timestamp(3) | Yes | Delivery date of the order |
| `order_cancelled_at` | timestamp(3) | Yes | Timestamp when the order was cancelled (if applicable) |
| `order_count` | integer | Yes | Order count field from the orders table |
| `status` | varchar | Yes | Current order status (e.g., delivered, void, rto) |
| `sub_status` | varchar | Yes | Order sub-status |
| `updated_status` | varchar | Yes | Status updated with RTO from cancelled_orders (rto if cancel_status is rto, else original status) |
| `uni_sales_order_date_ts` | timestamp(3) | Yes | Unicommerce sales order date |
| `uni_fulfillment_date_ts` | timestamp(3) | Yes | Unicommerce fulfillment date |
| `uni_shipping_code` | varchar | Yes | Unicommerce shipping code |
| `offline_store` | varchar | Yes | Offline store identifier (if applicable) |
| `is_bulk_order` | boolean | Yes | Whether this is a bulk order |
| `bulk_order_duration` | integer | Yes | Duration of bulk order in months |
| `is_combo` | boolean | Yes | Whether this is a combo order |
| `is_subscription_order` | boolean | Yes | Whether this is a subscription order |
| `is_international` | boolean | Yes | Whether this is an international order |
| `is_conditioner_free` | boolean | Yes | Whether conditioner was free with this order |
| `is_single_order` | boolean | Yes | Whether this is a single order |
| `discount_flag` | boolean | Yes | Whether a discount was applied |
| `is_offline_order` | boolean | Yes | Whether this is an offline order |
| `discount_code` | varchar | Yes | Discount code applied to the order |
| `coupon_code` | varchar | Yes | Coupon code extracted from order meta discount_applications |
| `utm_source` | varchar | Yes | UTM source tracking parameter |
| `utm_medium` | varchar | Yes | UTM medium tracking parameter |
| `utm_campaign` | varchar | Yes | UTM campaign tracking parameter |
| `referring_site` | varchar | Yes | Referring site URL |
| `landing_page_url` | varchar | Yes | Landing page URL for the order |
| `clinic_id` | varchar | Yes | Clinic identifier extracted from order meta note_attributes |
| `clinic_name` | varchar | Yes | Clinic name extracted from order meta note_attributes |
| `courier` | varchar | Yes | Tracking/courier company name |
| `tracking_id` | varchar | Yes | Shipment tracking ID |
| `tracking_url` | varchar | Yes | Shipment tracking URL |
| `order_meta_source_name` | varchar | Yes | Source name from order meta (e.g., web, app) |
| `order_meta_landing_site` | varchar | Yes | Landing site from order meta |
| `order_meta_landing_site_ref` | varchar | Yes | Landing site referrer from order meta |
| `order_meta_financial_status` | varchar | Yes | Financial status from order meta (e.g., paid, pending) |
| `gender` | varchar | Yes | Gender of the user |
| `user_created_at` | timestamp(3) | Yes | Timestamp when the user account was created |
| `is_lost_damaged` | boolean | Yes | Whether the order was lost or damaged |
| `refund_applicable` | boolean | Yes | Whether a refund is applicable for the cancelled order |
| `total_discount_amount` | double | Yes | Total discount amount applied to the order |
| `discount_type` | varchar | Yes | Type of discount applied |
| `coins_discount_amount` | double | Yes | Amount redeemed via Traya coins/rewards |
| `payment_gateway` | varchar | Yes | Payment gateway used for the order |
| `order_source` | varchar | Yes | Source of the order |
| `order_meta_tags` | varchar | Yes | Tags from order meta |
| `order_value` | double | Yes | Total order value (price) |
| `shipping_amount` | double | Yes | Shipping amount charged |
| `total_tax` | double | Yes | Total tax amount |
| `picked_up_at` | timestamp(3) | Yes | Timestamp when the shipment was picked up |
| `first_out_for_delivery_at` | timestamp(3) | Yes | Timestamp of first out-for-delivery attempt |
| `total_delivery_attempts` | integer | Yes | Total number of delivery attempts |
| `warehouse` | varchar | Yes | Warehouse name from which the order was fulfilled |
| `cp_code` | varchar | Yes | Courier partner code from order tracking |
| `sub_cp` | varchar | Yes | Sub courier partner from order tracking |
| `delivery_city` | varchar | Yes | Delivery city derived from pincode master |
| `zip` | varchar | Yes | Shipping address zip/pincode |
| `shipping_city` | varchar | Yes | Shipping address city |
| `country` | varchar | Yes | Shipping address country |
| `province` | varchar | Yes | Shipping address province/state |
| `delivery_promise_date_customer` | timestamp(3) | Yes | Estimated delivery date based on order creation + pincode TAT |
| `mark_date` | date | Yes | Date when the order was marked as cancelled/RTO |
| `activity_date` | varchar | Yes | Activity date partition column (string format) |
| `aud_updated_at` | timestamp(3) | Yes | Audit timestamp when this row was last written by dbt (IST) |
| `order_sequence` | bigint | Yes | Dense rank of order within the case (excludes void/rto), from ez_traya_int_order_sequence_info |

## traya_marts_ez.ez_traya_tickets

Incremental Iceberg mart for support tickets. Enriches tickets with comments, history, doctor consultations, call attempts, and CSAT feedback. Merge key: (ticket_id, doctor_consultation_id). Partitioned by bucket(ticket_id, 10). Timestamps converted to IST (UTC+5:30).

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `ticket_id` | varchar | Yes | Unique MongoDB ObjectId for the ticket record (primary key, from oid__id) |
| `createdat` | timestamp(6) | Yes | Timestamp when the ticket was created (IST, UTC+5:30) |
| `updatedat` | timestamp(6) | Yes | Timestamp when the ticket was last updated (IST, UTC+5:30) |
| `case_id` | varchar | Yes | Customer case identifier linked to this ticket |
| `priority` | varchar | Yes | Ticket priority level (e.g., LOW, MEDIUM, HIGH, URGENT) |
| `ticketnumber` | integer | Yes | Human-readable unique ticket number for support reference |
| `category` | varchar | Yes | Primary category of the ticket (e.g., Refund, Medical, Delivery) |
| `sub_category` | varchar | Yes | Sub-category providing further classification under the main category |
| `is_internal` | boolean | Yes | Flag indicating whether the ticket is internal (not customer-facing) |
| `flagged` | boolean | Yes | Flag indicating whether the ticket has been marked for special attention |
| `total_refund_price` | double | Yes | Total refund amount requested or processed for this ticket |
| `request_type` | varchar | Yes | Type of request raised in the ticket (e.g., Refund, Replacement, Query) |
| `refund_status` | varchar | Yes | Current status of the refund request (e.g., PENDING, APPROVED, REJECTED) |
| `remark` | varchar | Yes | Additional remarks or notes added by the support agent on the ticket |
| `source` | varchar | Yes | Channel through which the ticket was created (e.g., EMAIL, WHATSAPP, CALL) |
| `order_display_id` | varchar | Yes | Order display ID from the source system linked to this ticket |
| `status` | varchar | Yes | Current status of the ticket (e.g., OPEN, CLOSED, PENDING, RESOLVED) |
| `author_first_name` | varchar | Yes | First name of the agent or user who created the ticket |
| `current_assignment_first_name` | varchar | Yes | First name of the agent currently assigned to this ticket |
| `due_date` | timestamp(6) | Yes | Due date for ticket resolution (IST, UTC+5:30) |
| `doctor_call_attempt` | integer | Yes | Number of call attempts made by the doctor for this ticket |
| `doctor_assignment_count` | integer | Yes | Number of times this ticket has been assigned to a doctor |
| `medical_agent` | varchar | Yes | Identifier or name of the medical agent handling this ticket |
| `is_inline_transfer_enabled` | boolean | Yes | Flag indicating whether inline transfer is enabled for this ticket |
| `is_customer_risky` | boolean | Yes | Flag indicating whether the customer associated is marked as risky |
| `medical_slot_id` | varchar | Yes | Identifier for the medical slot booked in relation to this ticket |
| `is_valid` | boolean | Yes | Flag indicating whether the ticket record is valid and active |
| `escalation_count` | integer | Yes | Total number of times the ticket was escalated |
| `first_comment` | varchar | Yes | Description text of the first comment posted on the ticket (chronologically) |
| `first_commented_by` | varchar | Yes | First name of the agent who posted the first comment on the ticket |
| `first_comment_created_at` | timestamp(6) | Yes | Timestamp when the first comment was posted (IST, UTC+5:30) |
| `last_comment` | varchar | Yes | Description text of the most recent comment posted on the ticket |
| `last_commented_by` | varchar | Yes | First name of the agent who posted the most recent comment |
| `last_comment_created_at` | timestamp(6) | Yes | Timestamp when the most recent comment was posted (IST, UTC+5:30) |
| `last_action_description` | varchar | Yes | Description of the most recent action or state change in ticket history |
| `last_action_by` | varchar | Yes | First name of the agent who performed the most recent action |
| `last_action_time` | timestamp(6) | Yes | Timestamp of the most recent action in ticket history (IST, UTC+5:30) |
| `reopened_time` | timestamp(6) | Yes | Timestamp of the most recent TICKET_OPENED_AND_ESCALATED event (IST) |
| `reopened_count` | integer | Yes | Total number of TICKET_OPENED_AND_ESCALATED events |
| `doctor_consultation_id` | varchar | Yes | Unique identifier for the doctor consultation session linked to this ticket |
| `comment` | varchar | Yes | Doctor consultation comment text |
| `latest_calling_system_time` | timestamp(6) | Yes | Doctor consultation reminder date converted to IST (UTC+5:30) |
| `doctor_name` | varchar | Yes | Full name of the doctor assigned to this consultation |
| `doctor_id` | varchar | Yes | Unique identifier for the doctor assigned to this consultation |
| `doctor_call_status` | varchar | Yes | Doctor call outcome: answered (finished + comment != unanswered), unanswered, or NULL |
| `first_attempt_start` | varchar | Yes | Timestamp when the first doctor call attempt was initiated (IST string) |
| `first_call_result` | varchar | Yes | Outcome of the first doctor call attempt (e.g., CONNECTED, NOT_ANSWERED, BUSY) |
| `first_attempt_user_id` | varchar | Yes | ID of the agent who made the first call attempt |
| `second_attempt_start` | varchar | Yes | Timestamp when the second doctor call attempt was initiated (IST string) |
| `second_call_result` | varchar | Yes | Outcome of the second doctor call attempt |
| `second_attempt_user_id` | varchar | Yes | ID of the agent who made the second call attempt |
| `csat_response` | varchar | Yes | Customer satisfaction score or response collected after ticket resolution |
| `followup_message` | varchar | Yes | Follow-up message sent to the customer after ticket closure |
| `doctor_email` | varchar | Yes | Email address of the doctor assigned to this consultation |
| `first_attempt_user` | varchar | Yes | Name of the agent who made the first call attempt |
| `second_attempt_user` | varchar | Yes | Name of the agent who made the second call attempt |

## traya_marts_ez.ez_traya_tickets_vw

View on ez_traya_tickets. Same schema and semantics as the base Iceberg table.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `ticket_id` | varchar | Yes | Unique MongoDB ObjectId for the ticket record (primary key, from oid__id) |
| `createdat` | timestamp(3) | Yes | Timestamp when the ticket was created (IST, UTC+5:30) |
| `updatedat` | timestamp(3) | Yes | Timestamp when the ticket was last updated (IST, UTC+5:30) |
| `case_id` | varchar | Yes | Customer case identifier linked to this ticket |
| `priority` | varchar | Yes | Ticket priority level (e.g., LOW, MEDIUM, HIGH, URGENT) |
| `ticketnumber` | integer | Yes | Human-readable unique ticket number for support reference |
| `category` | varchar | Yes | Primary category of the ticket (e.g., Refund, Medical, Delivery) |
| `sub_category` | varchar | Yes | Sub-category providing further classification under the main category |
| `is_internal` | boolean | Yes | Flag indicating whether the ticket is internal (not customer-facing) |
| `flagged` | boolean | Yes | Flag indicating whether the ticket has been marked for special attention |
| `total_refund_price` | double | Yes | Total refund amount requested or processed for this ticket |
| `request_type` | varchar | Yes | Type of request raised in the ticket (e.g., Refund, Replacement, Query) |
| `refund_status` | varchar | Yes | Current status of the refund request (e.g., PENDING, APPROVED, REJECTED) |
| `remark` | varchar | Yes | Additional remarks or notes added by the support agent on the ticket |
| `source` | varchar | Yes | Channel through which the ticket was created (e.g., EMAIL, WHATSAPP, CALL) |
| `order_display_id` | varchar | Yes | Order display ID from the source system linked to this ticket |
| `status` | varchar | Yes | Current status of the ticket (e.g., OPEN, CLOSED, PENDING, RESOLVED) |
| `author_first_name` | varchar | Yes | First name of the agent or user who created the ticket |
| `current_assignment_first_name` | varchar | Yes | First name of the agent currently assigned to this ticket |
| `due_date` | timestamp(3) | Yes | Due date for ticket resolution (IST, UTC+5:30) |
| `doctor_call_attempt` | integer | Yes | Number of call attempts made by the doctor for this ticket |
| `doctor_assignment_count` | integer | Yes | Number of times this ticket has been assigned to a doctor |
| `medical_agent` | varchar | Yes | Identifier or name of the medical agent handling this ticket |
| `is_inline_transfer_enabled` | boolean | Yes | Flag indicating whether inline transfer is enabled for this ticket |
| `is_customer_risky` | boolean | Yes | Flag indicating whether the customer associated is marked as risky |
| `medical_slot_id` | varchar | Yes | Identifier for the medical slot booked in relation to this ticket |
| `is_valid` | boolean | Yes | Flag indicating whether the ticket record is valid and active |
| `escalation_count` | integer | Yes | Total number of times the ticket was escalated |
| `first_comment` | varchar | Yes | Description text of the first comment posted on the ticket (chronologically) |
| `first_commented_by` | varchar | Yes | First name of the agent who posted the first comment on the ticket |
| `first_comment_created_at` | timestamp(3) | Yes | Timestamp when the first comment was posted (IST, UTC+5:30) |
| `last_comment` | varchar | Yes | Description text of the most recent comment posted on the ticket |
| `last_commented_by` | varchar | Yes | First name of the agent who posted the most recent comment |
| `last_comment_created_at` | timestamp(3) | Yes | Timestamp when the most recent comment was posted (IST, UTC+5:30) |
| `last_action_description` | varchar | Yes | Description of the most recent action or state change in ticket history |
| `last_action_by` | varchar | Yes | First name of the agent who performed the most recent action |
| `last_action_time` | timestamp(3) | Yes | Timestamp of the most recent action in ticket history (IST, UTC+5:30) |
| `reopened_time` | timestamp(3) | Yes | Timestamp of the most recent TICKET_OPENED_AND_ESCALATED event (IST) |
| `reopened_count` | integer | Yes | Total number of TICKET_OPENED_AND_ESCALATED events |
| `doctor_consultation_id` | varchar | Yes | Unique identifier for the doctor consultation session linked to this ticket |
| `comment` | varchar | Yes | Doctor consultation comment text |
| `latest_calling_system_time` | timestamp(3) | Yes | Doctor consultation reminder date converted to IST (UTC+5:30) |
| `doctor_name` | varchar | Yes | Full name of the doctor assigned to this consultation |
| `doctor_id` | varchar | Yes | Unique identifier for the doctor assigned to this consultation |
| `doctor_call_status` | varchar | Yes | Doctor call outcome: answered (finished + comment != unanswered), unanswered, or NULL |
| `first_attempt_start` | varchar | Yes | Timestamp when the first doctor call attempt was initiated (IST string) |
| `first_call_result` | varchar | Yes | Outcome of the first doctor call attempt (e.g., CONNECTED, NOT_ANSWERED, BUSY) |
| `first_attempt_user_id` | varchar | Yes | ID of the agent who made the first call attempt |
| `second_attempt_start` | varchar | Yes | Timestamp when the second doctor call attempt was initiated (IST string) |
| `second_call_result` | varchar | Yes | Outcome of the second doctor call attempt |
| `second_attempt_user_id` | varchar | Yes | ID of the agent who made the second call attempt |
| `csat_response` | varchar | Yes | Customer satisfaction score or response collected after ticket resolution |
| `followup_message` | varchar | Yes | Follow-up message sent to the customer after ticket closure |
| `doctor_email` | varchar | Yes | Email address of the doctor assigned to this consultation |
| `first_attempt_user` | varchar | Yes | Name of the agent who made the first call attempt |
| `second_attempt_user` | varchar | Yes | Name of the agent who made the second call attempt |

## traya_marts_ez.ez_traya_users_profile

Canonical user profile mart. One row per user (case). Combines user demographics, latest form response (overall, app, web), age (from question C1d), location (zip/state/city from latest order's pincode), and order statistics. Derived flags: `is_purchaser`, `is_o3_plus`, `customer_segment` (lead/new_customer/loyal_customer). Iceberg table, partitioned by bucket(case_id, 16). Use for audience segmentation, funnel analysis, and user profiling.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `user_id` | varchar | Yes | Unique user identifier from the users table |
| `case_id` | varchar | Yes | Unique case identifier linked to the user |
| `first_name` | varchar | Yes | First name of the user |
| `email` | varchar | Yes | Email address of the user |
| `phone_number` | varchar | Yes | Phone number of the user |
| `gender` | varchar | Yes | Gender of the user |
| `latest_form_status` | varchar | Yes | Status of the most recent form response submitted by the user |
| `form_fill_source` | varchar | Yes | Source/channel through which the latest form was filled (e.g., app, web) |
| `latest_form_updated_at` | timestamp(6) | Yes | Timestamp when the latest form response was last updated |
| `latest_app_form_status` | varchar | Yes | Status of the most recent form response submitted via the app |
| `latest_app_form_updated_at` | timestamp(6) | Yes | Timestamp when the latest app form response was last updated |
| `latest_web_form_status` | varchar | Yes | Status of the most recent form response submitted via the web |
| `latest_web_form_updated_at` | timestamp(6) | Yes | Timestamp when the latest web form response was last updated |
| `age` | integer | Yes | Age of the user derived from form response (question C1d) |
| `zip` | varchar | Yes | Shipping zip code from the latest order's shipping address |
| `state` | varchar | Yes | State derived from the latest order's shipping zip via ots_pincode_masters_vw |
| `city` | varchar | Yes | City derived from the latest order's shipping address zip via pincode_mapping_vw |
| `total_orders` | bigint | Yes | Total number of orders placed by the user (defaults to 0 if none) |
| `latest_order_date` | date | Yes | Date of the user's most recent order |
| `first_order_date` | date | Yes | Date of the user's first order |
| `latest_order_updated_at` | timestamp(6) | Yes | Timestamp when the user's most recent order was last updated |
| `has_app_orders` | boolean | Yes | Flag indicating whether the user has placed orders via the app |
| `has_web_orders` | boolean | Yes | Flag indicating whether the user has placed orders via the web |
| `is_purchaser` | boolean | Yes | Flag indicating whether the user has placed at least one order |
| `is_o3_plus` | boolean | Yes | Flag indicating whether the user has placed more than 3 orders |
| `customer_segment` | varchar | Yes | User segment based on order count: lead (0), new_customer (1-3), or loyal_customer (4+) |

## traya_marts_ez.ez_traya_users_profile_vw

View on ez_traya_users_profile. Same schema and semantics as the base Iceberg table.

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `user_id` | varchar | Yes | Unique user identifier from the users table |
| `case_id` | varchar | Yes | Unique case identifier linked to the user |
| `first_name` | varchar | Yes | First name of the user |
| `email` | varchar | Yes | Email address of the user |
| `phone_number` | varchar | Yes | Phone number of the user |
| `gender` | varchar | Yes | Gender of the user |
| `latest_form_status` | varchar | Yes | Status of the most recent form response submitted by the user |
| `form_fill_source` | varchar | Yes | Source/channel through which the latest form was filled (e.g., app, web) |
| `latest_form_updated_at` | timestamp(3) | Yes | Timestamp when the latest form response was last updated |
| `latest_app_form_status` | varchar | Yes | Status of the most recent form response submitted via the app |
| `latest_app_form_updated_at` | timestamp(3) | Yes | Timestamp when the latest app form response was last updated |
| `latest_web_form_status` | varchar | Yes | Status of the most recent form response submitted via the web |
| `latest_web_form_updated_at` | timestamp(3) | Yes | Timestamp when the latest web form response was last updated |
| `age` | integer | Yes | Age of the user derived from form response (question C1d) |
| `zip` | varchar | Yes | Shipping zip code from the latest order's shipping address |
| `state` | varchar | Yes | State derived from the latest order's shipping zip via ots_pincode_masters_vw |
| `city` | varchar | Yes | City derived from the latest order's shipping address zip via pincode_mapping_vw |
| `total_orders` | bigint | Yes | Total number of orders placed by the user (defaults to 0 if none) |
| `latest_order_date` | date | Yes | Date of the user's most recent order |
| `first_order_date` | date | Yes | Date of the user's first order |
| `latest_order_updated_at` | timestamp(3) | Yes | Timestamp when the user's most recent order was last updated |
| `has_app_orders` | boolean | Yes | Flag indicating whether the user has placed orders via the app |
| `has_web_orders` | boolean | Yes | Flag indicating whether the user has placed orders via the web |
| `is_purchaser` | boolean | Yes | Flag indicating whether the user has placed at least one order |
| `is_o3_plus` | boolean | Yes | Flag indicating whether the user has placed more than 3 orders |
| `customer_segment` | varchar | Yes | User segment based on order count: lead (0), new_customer (1-3), or loyal_customer (4+) |

## trayaprod.abandoned_carts_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `amount` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `checkout_id` | varchar | Yes |  |
| `checkout_url` | varchar | Yes |  |
| `createdat` | varchar | Yes |  |
| `discount_code` | varchar | Yes |  |
| `meta_abandoned_checkout_url` | varchar | Yes |  |
| `meta_billing_address` | varchar | Yes |  |
| `meta_buyer_accepts_marketing` | boolean | Yes |  |
| `meta_cart_product_ids` | varchar | Yes |  |
| `meta_cart_product_names` | varchar | Yes |  |
| `meta_cart_token` | varchar | Yes |  |
| `meta_cart_variant_ids` | varchar | Yes |  |
| `meta_case_id` | varchar | Yes |  |
| `meta_checkout_id` | varchar | Yes |  |
| `meta_checkout_status` | varchar | Yes |  |
| `meta_closed_at` | varchar | Yes |  |
| `meta_coin_redemption` | varchar | Yes |  |
| `meta_completed_at` | varchar | Yes |  |
| `meta_createdat` | varchar | Yes |  |
| `meta_created_at` | varchar | Yes |  |
| `meta_currency` | varchar | Yes |  |
| `meta_customer` | varchar | Yes |  |
| `meta_customer_locale` | varchar | Yes |  |
| `meta_device_id` | varchar | Yes |  |
| `meta_discount` | varchar | Yes |  |
| `meta_discount_amount` | varchar | Yes |  |
| `meta_discount_codes` | varchar | Yes |  |
| `meta_email` | varchar | Yes |  |
| `meta_event_name` | varchar | Yes |  |
| `meta_final_amount` | varchar | Yes |  |
| `meta_gateway` | varchar | Yes |  |
| `meta_id` | varchar | Yes |  |
| `meta_image_url` | varchar | Yes |  |
| `meta_item_title_list` | varchar | Yes |  |
| `meta_landing_page_url` | varchar | Yes |  |
| `meta_landing_site` | varchar | Yes |  |
| `meta_line_items` | varchar | Yes |  |
| `meta_location_id` | varchar | Yes |  |
| `meta_name` | varchar | Yes |  |
| `meta_note` | varchar | Yes |  |
| `meta_note_attributes` | varchar | Yes |  |
| `meta_order_meta` | varchar | Yes |  |
| `meta_order_source` | varchar | Yes |  |
| `meta_order_type` | varchar | Yes |  |
| `meta_page_drop_event` | varchar | Yes |  |
| `meta_payment` | varchar | Yes |  |
| `meta_payment_order_id` | varchar | Yes |  |
| `meta_payment_service` | varchar | Yes |  |
| `meta_phone` | varchar | Yes |  |
| `meta_placed_from_webhook` | boolean | Yes |  |
| `meta_presentment_currency` | varchar | Yes |  |
| `meta_provider_order_id` | varchar | Yes |  |
| `meta_referring_site` | varchar | Yes |  |
| `meta_session_id` | varchar | Yes |  |
| `meta_shipping_address` | varchar | Yes |  |
| `meta_shipping_charges` | varchar | Yes |  |
| `meta_shipping_lines` | varchar | Yes |  |
| `meta_shopify_order_display_id` | varchar | Yes |  |
| `meta_source` | varchar | Yes |  |
| `meta_source_identifier` | varchar | Yes |  |
| `meta_source_name` | varchar | Yes |  |
| `meta_source_url` | varchar | Yes |  |
| `meta_subtotal_price` | varchar | Yes |  |
| `meta_tax_lines` | varchar | Yes |  |
| `meta_taxes_included` | boolean | Yes |  |
| `meta_timestamp` | double | Yes |  |
| `meta_token` | varchar | Yes |  |
| `meta_token_id` | varchar | Yes |  |
| `meta_total_discount` | double | Yes |  |
| `meta_total_discounts` | varchar | Yes |  |
| `meta_total_duties` | varchar | Yes |  |
| `meta_total_line_items_price` | varchar | Yes |  |
| `meta_total_price` | varchar | Yes |  |
| `meta_total_shipping` | bigint | Yes |  |
| `meta_total_tax` | varchar | Yes |  |
| `meta_total_weight` | bigint | Yes |  |
| `meta_updatedat` | varchar | Yes |  |
| `meta_updated_at` | varchar | Yes |  |
| `meta_user_id` | varchar | Yes |  |
| `meta_user_type` | varchar | Yes |  |
| `meta_utm_params` | varchar | Yes |  |
| `phone_number` | varchar | Yes |  |
| `province` | varchar | Yes |  |
| `shopflo_checkout_url` | varchar | Yes |  |
| `source` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `updatedat` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `utm_campaign` | varchar | Yes |  |
| `utm_medium` | varchar | Yes |  |
| `utm_source` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.app_and_user_details_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `age` | varchar | Yes |  |
| `app_version` | varchar | Yes |  |
| `brand` | varchar | Yes |  |
| `build_number` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `city` | varchar | Yes |  |
| `country_code` | varchar | Yes |  |
| `country_name` | varchar | Yes |  |
| `gender` | varchar | Yes |  |
| `ip_address` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `model` | varchar | Yes |  |
| `os_version` | varchar | Yes |  |
| `pin_code` | varchar | Yes |  |
| `platform` | varchar | Yes |  |
| `state` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `ota_current_version` | varchar | Yes |  |
| `ota_error_message` | varchar | Yes |  |
| `ota_update_success` | boolean | Yes |  |
| `ota_update_version` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.call_provider_webhook_data_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `activity_tracking_processed_at` | timestamp(3) | Yes |  |
| `activity_tracking_status` | varchar | Yes |  |
| `attempt_id` | varchar | Yes |  |
| `caller_user_id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `direction` | varchar | Yes |  |
| `disposition_code` | varchar | Yes |  |
| `end_time` | varchar | Yes |  |
| `end_time_utc` | timestamp(3) | Yes |  |
| `engagement_id` | varchar | Yes |  |
| `is_adhoc_call` | boolean | Yes |  |
| `phone` | varchar | Yes |  |
| `provider` | varchar | Yes |  |
| `raw_payload_custom_fields` | varchar | Yes |  |
| `raw_payload_direction` | varchar | Yes |  |
| `raw_payload_disposition_code` | varchar | Yes |  |
| `raw_payload_end_time` | varchar | Yes |  |
| `raw_payload_phone` | varchar | Yes |  |
| `raw_payload_ringing_time` | varchar | Yes |  |
| `raw_payload_sid` | varchar | Yes |  |
| `raw_payload_start_time` | varchar | Yes |  |
| `raw_payload_status` | varchar | Yes |  |
| `raw_payload_total_talk_time` | varchar | Yes |  |
| `raw_payload_url` | varchar | Yes |  |
| `raw_payload_user_id` | varchar | Yes |  |
| `raw_payload_virtual_number` | varchar | Yes |  |
| `recording_url` | varchar | Yes |  |
| `ringing_time` | bigint | Yes |  |
| `sid` | varchar | Yes |  |
| `start_time` | varchar | Yes |  |
| `start_time_utc` | timestamp(3) | Yes |  |
| `status` | varchar | Yes |  |
| `total_duration_seconds` | bigint | Yes |  |
| `total_talk_time` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `virtual_number` | varchar | Yes |  |
| `webhooktype` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.case_responses_recommendations_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `responses_order_value` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.case_summaries_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `generated_timestamp` | timestamp(3) | Yes |  |
| `input_tokens` | bigint | Yes |  |
| `output_tokens` | bigint | Yes |  |
| `payload_to_generate_summary` | varchar | Yes |  |
| `summary` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.checkout_carts_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `checkout_status` | varchar | Yes |  |
| `coin_redemption` | varchar | Yes |  |
| `customer` | varchar | Yes |  |
| `discount` | varchar | Yes |  |
| `discount_amount` | varchar | Yes |  |
| `final_amount` | varchar | Yes |  |
| `is_refunded` | boolean | Yes |  |
| `landing_page_url` | varchar | Yes |  |
| `line_items` | varchar | Yes |  |
| `note_attributes` | varchar | Yes |  |
| `order_meta` | varchar | Yes |  |
| `order_placed_to` | varchar | Yes |  |
| `order_source` | varchar | Yes |  |
| `order_status` | varchar | Yes |  |
| `order_type` | varchar | Yes |  |
| `payment` | varchar | Yes |  |
| `payment_order_id` | varchar | Yes |  |
| `payment_service` | varchar | Yes |  |
| `placed_from_webhook` | boolean | Yes |  |
| `provider_order_id` | varchar | Yes |  |
| `provider_payment_id` | varchar | Yes |  |
| `refund_id` | varchar | Yes |  |
| `refund_rrn` | varchar | Yes |  |
| `refund_source` | varchar | Yes |  |
| `session_id` | varchar | Yes |  |
| `shipping_address` | varchar | Yes |  |
| `shipping_charges` | varchar | Yes |  |
| `shopify_order_display_id` | varchar | Yes |  |
| `total_amount_paid` | varchar | Yes |  |
| `total_price` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `user_type` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.checkout_events_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `cart_products` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `event_name` | varchar | Yes |  |
| `kit_type_purchased` | bigint | Yes |  |
| `order_count` | bigint | Yes |  |
| `order_display_id` | varchar | Yes |  |
| `platform` | varchar | Yes |  |
| `session_id` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `total_order_value` | bigint | Yes |  |
| `user_id` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.clinicpeople_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `clinic_id` | varchar | Yes |  |
| `email` | varchar | Yes |  |
| `emp_code` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `name` | varchar | Yes |  |
| `phone_number` | varchar | Yes |  |
| `type` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.clinics_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `address` | varchar | Yes |  |
| `area` | varchar | Yes |  |
| `city` | varchar | Yes |  |
| `clinic_id` | varchar | Yes |  |
| `clinic_name` | varchar | Yes |  |
| `clinic_persons` | varchar | Yes |  |
| `community_tag` | varchar | Yes |  |
| `country` | varchar | Yes |  |
| `country_code` | varchar | Yes |  |
| `device_list` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `locality` | varchar | Yes |  |
| `location` | varchar | Yes |  |
| `location_coordinates` | varchar | Yes |  |
| `pincode` | bigint | Yes |  |
| `province` | varchar | Yes |  |
| `type` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.convin_call_summaries_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `api_status` | varchar | Yes |  |
| `call_id` | varchar | Yes |  |
| `convin_data_agent_id` | varchar | Yes |  |
| `convin_data_agent_name` | varchar | Yes |  |
| `convin_data_attempt_end` | varchar | Yes |  |
| `convin_data_attempt_start` | varchar | Yes |  |
| `convin_data_callid` | varchar | Yes |  |
| `convin_data_call_id` | varchar | Yes |  |
| `convin_data_call_time` | varchar | Yes |  |
| `convin_data_call_type` | varchar | Yes |  |
| `convin_data_caller_number` | varchar | Yes |  |
| `convin_data_customer_id` | varchar | Yes |  |
| `convin_data_engagementid` | varchar | Yes |  |
| `convin_data_engagement_id` | varchar | Yes |  |
| `convin_data_is_slot_type` | boolean | Yes |  |
| `convin_data_language_identifier` | varchar | Yes |  |
| `convin_data_order_id` | varchar | Yes |  |
| `convin_data_receivedat` | varchar | Yes |  |
| `convin_data_recordingfile_url` | varchar | Yes |  |
| `convin_data_source_dialer` | varchar | Yes |  |
| `convin_data_summary` | varchar | Yes |  |
| `convin_data_talk_time` | varchar | Yes |  |
| `convin_data_timezone` | varchar | Yes |  |
| `convin_data_transcript` | varchar | Yes |  |
| `convin_data_type_of_call` | varchar | Yes |  |
| `engagement_id` | varchar | Yes |  |
| `retry_count` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.csat_feedback_responses_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `agent_email` | varchar | Yes |  |
| `agent_id` | varchar | Yes |  |
| `agent_level` | varchar | Yes |  |
| `agent_role` | varchar | Yes |  |
| `call_sid` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `customer_gender` | varchar | Yes |  |
| `customer_language` | varchar | Yes |  |
| `customer_phone` | varchar | Yes |  |
| `engagement_id` | varchar | Yes |  |
| `engagement_tag` | varchar | Yes |  |
| `followup_messages` | varchar | Yes |  |
| `is_ivr_merged` | boolean | Yes |  |
| `is_slot_merged` | boolean | Yes |  |
| `response` | varchar | Yes |  |
| `ticket_category` | varchar | Yes |  |
| `ticket_id` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |

## trayaprod.csatfeedbacks_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `agent` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `change_coach` | bigint | Yes |  |
| `doubt_resolved` | bigint | Yes |  |
| `engagement` | varchar | Yes |  |
| `happy_with_traya` | bigint | Yes |  |
| `preffered_language` | varchar | Yes |  |
| `rate_your_coach` | bigint | Yes |  |
| `store_feedback` | boolean | Yes |  |
| `tag` | varchar | Yes |  |
| `tell_us_more` | varchar | Yes |  |
| `txn` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.customerfeedbacks_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `adherence_reason` | varchar | Yes |  |
| `any_product_reaction` | varchar | Yes |  |
| `cart_link` | varchar | Yes |  |
| `cart_link_3m` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `comment` | varchar | Yes |  |
| `concerns` | varchar | Yes |  |
| `constipation` | varchar | Yes |  |
| `customer_adherence` | varchar | Yes |  |
| `dandruff_feedback` | varchar | Yes |  |
| `diet` | varchar | Yes |  |
| `digestion` | varchar | Yes |  |
| `energy` | bigint | Yes |  |
| `engagement_id` | varchar | Yes |  |
| `gut_health` | bigint | Yes |  |
| `hair_breakage` | varchar | Yes |  |
| `hair_feedback` | varchar | Yes |  |
| `hair_growth` | bigint | Yes |  |
| `hair_loss` | bigint | Yes |  |
| `happy_with_traya` | bigint | Yes |  |
| `mood` | bigint | Yes |  |
| `not_ordering_reason` | varchar | Yes |  |
| `order_display_id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `overall_health` | varchar | Yes |  |
| `pre_cart_link` | varchar | Yes |  |
| `preffered_language` | varchar | Yes |  |
| `productrecommendations` | varchar | Yes |  |
| `product_reaction` | varchar | Yes |  |
| `rep_id` | varchar | Yes |  |
| `santulan_feedback` | varchar | Yes |  |
| `scalp_feedback` | varchar | Yes |  |
| `tag` | varchar | Yes |  |
| `user` | varchar | Yes |  |
| `actual_date` | timestamp(3) | Yes |  |
| `reminder_date` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.doctor_activity_trackings_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `attempt_count` | bigint | Yes |  |
| `attempts` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `doctor_consultation_id` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `version` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.doctor_order_edit_logs_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `doctor_id` | varchar | Yes |  |
| `meta_add` | varchar | Yes |  |
| `meta_remove` | varchar | Yes |  |
| `order_display_id` | varchar | Yes |  |
| `type` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.doctorconsulations_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `id` | varchar | Yes |  |
| `amount` | varchar | Yes |  |
| `assignment_email` | varchar | Yes |  |
| `assignment_first_name` | varchar | Yes |  |
| `assignment_id` | varchar | Yes |  |
| `booking_type` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `comment` | varchar | Yes |  |
| `consult_comment` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `currency` | varchar | Yes |  |
| `from_crm` | boolean | Yes |  |
| `isfollowup` | boolean | Yes |  |
| `isretention` | boolean | Yes |  |
| `isvalid` | boolean | Yes |  |
| `is_auto_finished` | boolean | Yes |  |
| `is_finished` | boolean | Yes |  |
| `is_rescheduled` | boolean | Yes |  |
| `is_user_booked` | boolean | Yes |  |
| `meta` | varchar | Yes |  |
| `offline_appointments` | bigint | Yes |  |
| `payment_id` | varchar | Yes |  |
| `payment_status` | varchar | Yes |  |
| `reminder_date` | timestamp(3) | Yes |  |
| `request_type` | varchar | Yes |  |
| `reschedule_count` | bigint | Yes |  |
| `ticket_id` | varchar | Yes |  |
| `unanswered_count` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `updated_at` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `video_meet_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.doctors_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `address_details` | varchar | Yes |  |
| `city_name` | varchar | Yes |  |
| `doctor_experiences` | varchar | Yes |  |
| `doctor_fee` | varchar | Yes |  |
| `doctor_name` | varchar | Yes |  |
| `doctor_profile` | varchar | Yes |  |
| `doctor_specialization` | varchar | Yes |  |
| `education_detail` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `specialities_detail` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.engagement_activity_trackings_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `attempt_count` | bigint | Yes |  |
| `attempts` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `customer_attributes_gender` | varchar | Yes |  |
| `customer_attributes_user_id` | varchar | Yes |  |
| `engagement_id` | varchar | Yes |  |
| `running_month` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `version` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.engagement_call_attempts_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `assigned_user_id` | varchar | Yes |  |
| `attempt_count` | bigint | Yes |  |
| `attempted_user_id` | varchar | Yes |  |
| `call_direction` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `crm_call_duration` | varchar | Yes |  |
| `crm_end_time` | timestamp(3) | Yes |  |
| `crm_start_time` | timestamp(3) | Yes |  |
| `customer_attributes_gender` | varchar | Yes |  |
| `customer_attributes_running_month` | varchar | Yes |  |
| `customer_attributes_user_id` | varchar | Yes |  |
| `engagement_id` | varchar | Yes |  |
| `is_ivr_attempt` | boolean | Yes |  |
| `ivr_webhook_id` | varchar | Yes |  |
| `provider` | varchar | Yes |  |
| `provider_agent_status` | varchar | Yes |  |
| `provider_call_duration` | varchar | Yes |  |
| `provider_call_sid` | varchar | Yes |  |
| `provider_call_status` | varchar | Yes |  |
| `provider_call_total_talk_time` | varchar | Yes |  |
| `provider_customer_status` | varchar | Yes |  |
| `provider_disposition_code` | varchar | Yes |  |
| `provider_end_time` | varchar | Yes |  |
| `provider_start_time` | varchar | Yes |  |
| `recording_url` | varchar | Yes |  |
| `reschedule_time` | timestamp(3) | Yes |  |
| `response__corrupt_record` | varchar | Yes |  |
| `response_adherence_reason` | varchar | Yes |  |
| `response_any_product_reaction` | varchar | Yes |  |
| `response_appinfo` | boolean | Yes |  |
| `response_beforetreatment` | varchar | Yes |  |
| `response_breakuptimeline` | varchar | Yes |  |
| `response_breakuptimelineexpectation` | varchar | Yes |  |
| `response_callresponse` | varchar | Yes |  |
| `response_call_type` | varchar | Yes |  |
| `response_category` | varchar | Yes |  |
| `response_clinicvisit` | varchar | Yes |  |
| `response_comment` | varchar | Yes |  |
| `response_comments` | varchar | Yes |  |
| `response_constipation` | bigint | Yes |  |
| `response_crmmentionedtime` | varchar | Yes |  |
| `response_crmmentionedtimecomments` | varchar | Yes |  |
| `response_customer_adherence` | varchar | Yes |  |
| `response_cx_wants_callback` | boolean | Yes |  |
| `response_dandruff` | bigint | Yes |  |
| `response_did_not_pick_up` | boolean | Yes |  |
| `response_dnd` | boolean | Yes |  |
| `response_doctor_intervention_required` | boolean | Yes |  |
| `response_dont_want_talk` | boolean | Yes |  |
| `response_dosageinfoflag` | boolean | Yes |  |
| `response_energy` | bigint | Yes |  |
| `response_femalepreg` | boolean | Yes |  |
| `response_guthealth` | bigint | Yes |  |
| `response_gut_health` | bigint | Yes |  |
| `response_hairgrowth` | bigint | Yes |  |
| `response_hairloss` | bigint | Yes |  |
| `response_hair_growth` | bigint | Yes |  |
| `response_hair_loss` | bigint | Yes |  |
| `response_healthcondition` | varchar | Yes |  |
| `response_healthconditioncomment` | varchar | Yes |  |
| `response_herbalflag` | boolean | Yes |  |
| `response_interested_in_community` | varchar | Yes |  |
| `response_is_valid_claim` | boolean | Yes |  |
| `response_kitinfoflag` | boolean | Yes |  |
| `response_language` | varchar | Yes |  |
| `response_languagebarrier` | varchar | Yes |  |
| `response_languagekey` | varchar | Yes |  |
| `response_medical_condition` | varchar | Yes |  |
| `response_medication_allergy` | varchar | Yes |  |
| `response_minoxidilinformed` | boolean | Yes |  |
| `response_minoxidil_info` | varchar | Yes |  |
| `response_mood` | bigint | Yes |  |
| `response_notpickedupreason` | varchar | Yes |  |
| `response_not_ordering_reason` | varchar | Yes |  |
| `response_note` | varchar | Yes |  |
| `response_ongoing_treatment` | varchar | Yes |  |
| `response_order_not_placed_reason` | varchar | Yes |  |
| `response_order_status` | varchar | Yes |  |
| `response_otherconcern` | varchar | Yes |  |
| `response_other_concern` | varchar | Yes |  |
| `response_other_issue` | varchar | Yes |  |
| `response_past_hair_treatment` | varchar | Yes |  |
| `response_pickedupreason` | varchar | Yes |  |
| `response_pickedupstatus` | varchar | Yes |  |
| `response_prevsupplementcomment` | varchar | Yes |  |
| `response_prevsupplementconsumed` | varchar | Yes |  |
| `response_product_reaction` | varchar | Yes |  |
| `response_queryinfo` | boolean | Yes |  |
| `response_reaction` | varchar | Yes |  |
| `response_reactions` | varchar | Yes |  |
| `response_reason` | varchar | Yes |  |
| `response_reasonfornotordering` | varchar | Yes |  |
| `response_reason_not_attending` | varchar | Yes |  |
| `response_reason_not_rescheduling` | varchar | Yes |  |
| `response_regularity` | varchar | Yes |  |
| `response_reschedule_scalp_test` | varchar | Yes |  |
| `response_response_category` | varchar | Yes |  |
| `response_response_tag` | varchar | Yes |  |
| `response_script_unfullfill` | boolean | Yes |  |
| `response_sleepstress` | bigint | Yes |  |
| `response_sleep_stress` | bigint | Yes |  |
| `response_slot_time` | varchar | Yes |  |
| `response_sub_category` | varchar | Yes |  |
| `response_tag` | varchar | Yes |  |
| `response_topical_os_informed` | boolean | Yes |  |
| `response_treatmentothercomment` | varchar | Yes |  |
| `response_treatmentstart` | varchar | Yes |  |
| `response_unanswered_reason` | varchar | Yes |  |
| `response_visit_confirmed` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `tag` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.engagements_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id` | varchar | Yes |  |
| `actual_date` | timestamp(3) | Yes |  |
| `attempt_count` | bigint | Yes |  |
| `batch` | bigint | Yes |  |
| `booking_reference_id` | varchar | Yes |  |
| `campaign` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `current` | boolean | Yes |  |
| `due_date` | timestamp(3) | Yes |  |
| `from_crm` | boolean | Yes |  |
| `is_finished` | boolean | Yes |  |
| `is_ivr_complete` | boolean | Yes |  |
| `is_slot_booked` | boolean | Yes |  |
| `is_valid` | boolean | Yes |  |
| `ivr_type` | varchar | Yes |  |
| `ivr_webhook_id` | varchar | Yes |  |
| `language` | varchar | Yes |  |
| `last_attempt` | timestamp(3) | Yes |  |
| `next_order_id` | varchar | Yes |  |
| `notes` | varchar | Yes |  |
| `operation_status` | varchar | Yes |  |
| `order_count` | bigint | Yes |  |
| `order_id` | varchar | Yes |  |
| `reference_tag` | varchar | Yes |  |
| `reminder_date` | timestamp(3) | Yes |  |
| `repeat_retention` | boolean | Yes |  |
| `repeat_retention_count` | bigint | Yes |  |
| `request_type` | varchar | Yes |  |
| `reschedule_count` | bigint | Yes |  |
| `running_month` | bigint | Yes |  |
| `slot_type` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `tag` | varchar | Yes |  |
| `temporary_assignment_id` | varchar | Yes |  |
| `temporary_user_id` | varchar | Yes |  |
| `unanswered_count` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `weight` | bigint | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.event_moengages_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `event_attributes` | varchar | Yes |  |
| `event_name` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.feedback_from_datas_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `form_name` | varchar | Yes |  |
| `meta_feedbackformtype` | varchar | Yes |  |
| `meta_utm_campaign` | varchar | Yes |  |
| `meta_utm_source` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `responses` | varchar | Yes |  |
| `meta_taskid` | varchar | Yes |  |
| `__v` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |

## trayaprod.freshchatmessages_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `chat_meta_actor` | varchar | Yes |  |
| `chat_meta_app` | varchar | Yes |  |
| `chat_meta_audio` | varchar | Yes |  |
| `chat_meta_button` | varchar | Yes |  |
| `chat_meta_contacts` | varchar | Yes |  |
| `chat_meta_context` | varchar | Yes |  |
| `chat_meta_converstation` | varchar | Yes |  |
| `chat_meta_document` | varchar | Yes |  |
| `chat_meta_forwarded` | boolean | Yes |  |
| `chat_meta_frequently_forwarded` | boolean | Yes |  |
| `chat_meta_image` | varchar | Yes |  |
| `chat_meta_interactive` | varchar | Yes |  |
| `chat_meta_location` | varchar | Yes |  |
| `chat_meta_messageid` | varchar | Yes |  |
| `chat_meta_mobile` | varchar | Yes |  |
| `chat_meta_name` | varchar | Yes |  |
| `chat_meta_payload` | varchar | Yes |  |
| `chat_meta_referral` | varchar | Yes |  |
| `chat_meta_replyid` | varchar | Yes |  |
| `chat_meta_text` | varchar | Yes |  |
| `chat_meta_timestamp` | timestamp(3) | Yes |  |
| `chat_meta_type` | varchar | Yes |  |
| `chat_meta_user` | varchar | Yes |  |
| `chat_meta_version` | bigint | Yes |  |
| `chat_meta_video` | varchar | Yes |  |
| `chat_meta_wanumber` | varchar | Yes |  |
| `chat_text` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `direction` | varchar | Yes |  |
| `params` | varchar | Yes |  |
| `receiver_phone` | varchar | Yes |  |
| `representative_id` | varchar | Yes |  |
| `sender_phone` | varchar | Yes |  |
| `source_id` | varchar | Yes |  |
| `template_id` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `chat_meta_appid` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.ivrwebhooks_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `callsid` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `customerphone` | varchar | Yes |  |
| `data_callfrom` | varchar | Yes |  |
| `data_callsid` | varchar | Yes |  |
| `data_callto` | varchar | Yes |  |
| `data_calltype` | varchar | Yes |  |
| `data_created` | varchar | Yes |  |
| `data_currenttime` | varchar | Yes |  |
| `data_detaileddialcallstatus` | varchar | Yes |  |
| `data_dialcallduration` | varchar | Yes |  |
| `data_dialcallstatus` | varchar | Yes |  |
| `data_dialwhomnumber` | varchar | Yes |  |
| `data_direction` | varchar | Yes |  |
| `data_endtime` | varchar | Yes |  |
| `data_enteredphone` | varchar | Yes |  |
| `data_from` | varchar | Yes |  |
| `data_legs` | varchar | Yes |  |
| `data_outgoingphonenumber` | varchar | Yes |  |
| `data_processstatus` | varchar | Yes |  |
| `data_recordingavailableby` | varchar | Yes |  |
| `data_recordingurl` | varchar | Yes |  |
| `data_starttime` | varchar | Yes |  |
| `data_to` | varchar | Yes |  |
| `data_actual_date` | varchar | Yes |  |
| `data_digits` | varchar | Yes |  |
| `data_end_time` | varchar | Yes |  |
| `data_engagement_id` | varchar | Yes |  |
| `data_flow_id` | varchar | Yes |  |
| `data_is_finished` | boolean | Yes |  |
| `data_leadivr` | boolean | Yes |  |
| `data_operation_status` | varchar | Yes |  |
| `data_request_type` | varchar | Yes |  |
| `data_source` | varchar | Yes |  |
| `data_start_time` | varchar | Yes |  |
| `data_status` | varchar | Yes |  |
| `data_tenant_id` | varchar | Yes |  |
| `isenteredphonenumber` | boolean | Yes |  |
| `isorder` | boolean | Yes |  |
| `isrepeatorder` | boolean | Yes |  |
| `isvaliduser` | boolean | Yes |  |
| `latest_order_id` | varchar | Yes |  |
| `orderstatus` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `wabasent` | boolean | Yes |  |
| `wabatemplate` | varchar | Yes |  |
| `webhooktype` | varchar | Yes |  |
| `data_forwardedfrom` | varchar | Yes |  |
| `data_hanguplatencystarttime` | varchar | Yes |  |
| `data_hanguplatencystarttimeexocc` | varchar | Yes |  |
| `data` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.login_logout_reports_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `duration` | bigint | Yes |  |
| `ipaddress` | varchar | Yes |  |
| `ismobile` | boolean | Yes |  |
| `logintime` | varchar | Yes |  |
| `logouttime` | varchar | Yes |  |
| `session_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.pincode_warehouse_mappings_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `pincode` | varchar | Yes |  |
| `warehouse` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.pincodes_masters_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `city` | varchar | Yes |  |
| `pincode` | varchar | Yes |  |
| `repeat_tat` | varchar | Yes |  |
| `state` | varchar | Yes |  |
| `state_code` | varchar | Yes |  |
| `tat` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.prescription_approval_requests_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `approved_by` | varchar | Yes |  |
| `approved_prescriptions` | varchar | Yes |  |
| `assigned_doctor` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `created_by` | varchar | Yes |  |
| `edit_history` | varchar | Yes |  |
| `edited_after_rejection` | boolean | Yes |  |
| `is_edited` | boolean | Yes |  |
| `is_locked_for_edit` | boolean | Yes |  |
| `last_edited_at` | varchar | Yes |  |
| `last_edited_by` | varchar | Yes |  |
| `prescription_items` | varchar | Yes |  |
| `proposed_prescriptions` | varchar | Yes |  |
| `rejection_reason` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `ticket_id` | varchar | Yes |  |
| `total_edit_count` | bigint | Yes |  |
| `version` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.redeem_reward_transactions_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `currency` | varchar | Yes |  |
| `order_display_id` | varchar | Yes |  |
| `order_id` | varchar | Yes |  |
| `redeemed_amount` | double | Yes |  |
| `redeemed_coins` | double | Yes |  |
| `remarks` | varchar | Yes |  |
| `shop_flo_txn_id` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.reorder_events_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `additional_products` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `event_name` | varchar | Yes |  |
| `maintenance_product_ids` | varchar | Yes |  |
| `next_month_recommended_cart` | varchar | Yes |  |
| `order_count` | bigint | Yes |  |
| `platform` | varchar | Yes |  |
| `session_id` | varchar | Yes |  |
| `total_order_value_1_month` | bigint | Yes |  |
| `total_order_value_3_month` | bigint | Yes |  |
| `upsell_products` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.reward_transactions_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `all_coins_used` | boolean | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `credit_coins` | double | Yes |  |
| `credit_remarks` | varchar | Yes |  |
| `debit_transactions` | varchar | Yes |  |
| `expire_at` | timestamp(3) | Yes |  |
| `is_credit_transaction` | boolean | Yes |  |
| `is_debit_transaction` | boolean | Yes |  |
| `status` | varchar | Yes |  |
| `streak_master_id` | varchar | Yes |  |
| `total_debit_coins` | double | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.streak_logs_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `longest_streak_days` | bigint | Yes |  |
| `streak_achieve_days` | bigint | Yes |  |
| `user_id` | varchar | Yes |  |
| `first_date_of_log` | timestamp(3) | Yes |  |
| `last_date_of_log` | timestamp(3) | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.streak_masters_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `days` | bigint | Yes |  |
| `display_name` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `is_for_superadmin` | boolean | Yes |  |
| `reward_coins` | bigint | Yes |  |
| `slug` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.task_masters_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `event_name` | varchar | Yes |  |
| `h1` | varchar | Yes |  |
| `h2` | varchar | Yes |  |
| `h3` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `navigation` | varchar | Yes |  |
| `priority` | bigint | Yes |  |
| `task_name` | varchar | Yes |  |
| `type` | varchar | Yes |  |
| `url_or_text` | varchar | Yes |  |
| `_priority__` | bigint | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.tickets_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `acl` | varchar | Yes |  |
| `address_city` | varchar | Yes |  |
| `address_landmark` | varchar | Yes |  |
| `address_locality` | varchar | Yes |  |
| `address_pincode` | varchar | Yes |  |
| `address_state` | varchar | Yes |  |
| `author_email` | varchar | Yes |  |
| `author_first_name` | varchar | Yes |  |
| `author_phone_number` | varchar | Yes |  |
| `author_user_id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `category` | varchar | Yes |  |
| `comments` | varchar | Yes |  |
| `created_at_against` | varchar | Yes |  |
| `current_assignment_email` | varchar | Yes |  |
| `current_assignment_first_name` | varchar | Yes |  |
| `current_assignment_phone_number` | varchar | Yes |  |
| `current_assignment_user_id` | varchar | Yes |  |
| `current_assignment_user_meta` | varchar | Yes |  |
| `customer_email` | varchar | Yes |  |
| `customer_first_name` | varchar | Yes |  |
| `customer_phone_number` | varchar | Yes |  |
| `customer_user_id` | varchar | Yes |  |
| `doctor_assignment_count` | bigint | Yes |  |
| `doctor_call_attempt` | bigint | Yes |  |
| `faq_display_name` | varchar | Yes |  |
| `flagged` | boolean | Yes |  |
| `history` | varchar | Yes |  |
| `images` | varchar | Yes |  |
| `is_inline_transfer_enabled` | boolean | Yes |  |
| `is_internal` | boolean | Yes |  |
| `is_valid` | boolean | Yes |  |
| `medical_agent` | varchar | Yes |  |
| `medical_slot_assignment` | varchar | Yes |  |
| `medical_slot_id` | varchar | Yes |  |
| `priority` | varchar | Yes |  |
| `priority_code` | varchar | Yes |  |
| `products` | varchar | Yes |  |
| `provider` | varchar | Yes |  |
| `provider_meta_description` | varchar | Yes |  |
| `provider_meta_descriptionvalue` | varchar | Yes |  |
| `provider_meta_due_date` | varchar | Yes |  |
| `provider_meta_subject` | varchar | Yes |  |
| `provider_ref_id` | varchar | Yes |  |
| `refund_status` | varchar | Yes |  |
| `remark` | varchar | Yes |  |
| `request_type` | varchar | Yes |  |
| `source` | varchar | Yes |  |
| `source_meta_callfrom` | varchar | Yes |  |
| `source_meta_callsid` | varchar | Yes |  |
| `source_meta_callto` | varchar | Yes |  |
| `source_meta_calltype` | varchar | Yes |  |
| `source_meta_created` | varchar | Yes |  |
| `source_meta_currenttime` | varchar | Yes |  |
| `source_meta_dialcallduration` | varchar | Yes |  |
| `source_meta_dialwhomnumber` | varchar | Yes |  |
| `source_meta_direction` | varchar | Yes |  |
| `source_meta_endtime` | varchar | Yes |  |
| `source_meta_from` | varchar | Yes |  |
| `source_meta_starttime` | varchar | Yes |  |
| `source_meta_to` | varchar | Yes |  |
| `source_meta_digits` | varchar | Yes |  |
| `source_meta_flow_id` | varchar | Yes |  |
| `source_meta_orderdetails` | varchar | Yes |  |
| `source_meta_order_details` | varchar | Yes |  |
| `source_meta_order_display_id` | varchar | Yes |  |
| `source_meta_order_id` | varchar | Yes |  |
| `source_meta_source` | varchar | Yes |  |
| `source_meta_tenant_id` | varchar | Yes |  |
| `source_meta_title` | varchar | Yes |  |
| `status` | varchar | Yes |  |
| `status_code` | varchar | Yes |  |
| `sub_category` | varchar | Yes |  |
| `ticketnumber` | bigint | Yes |  |
| `total_refund_price` | varchar | Yes |  |
| `version` | varchar | Yes |  |
| `escalation_count` | bigint | Yes |  |
| `author_user_meta` | varchar | Yes |  |
| `customer_user_meta` | varchar | Yes |  |
| `inline_transfer_slot_booking_reason` | varchar | Yes |  |
| `is_customer_risky` | boolean | Yes |  |
| `due_date` | timestamp(3) | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |

## trayaprod.user_activity_logs_for_bahs_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `_id` | varchar | Yes |  |
| `check_ins_for_date` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `is_active` | boolean | Yes |  |
| `is_valid_for_streak` | boolean | Yes |  |
| `product_prescriptions` | varchar | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `user_id` | varchar | Yes |  |
| `kafka_commit_time` | bigint | Yes |  |
| `_hoodie_commit_time` | varchar | Yes |  |
| `activity_date` | varchar | Yes |  |

## trayaprod.user_task_details_vw

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `oid__id` | varchar | Yes |  |
| `case_id` | varchar | Yes |  |
| `click_count` | bigint | Yes |  |
| `completed_by` | varchar | Yes |  |
| `is_active` | boolean | Yes |  |
| `order_id` | varchar | Yes |  |
| `task_completion_response` | varchar | Yes |  |
| `task_id` | varchar | Yes |  |
| `user_id` | varchar | Yes |  |
| `completed_date` | timestamp(3) | Yes |  |
| `start_date` | timestamp(3) | Yes |  |
| `due_date` | timestamp(3) | Yes |  |
| `updatedat` | timestamp(3) | Yes |  |
| `createdat` | timestamp(3) | Yes |  |
| `activity_date` | varchar | Yes |  |
