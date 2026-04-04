"""MCP Server for AWS Athena queries.

Runs locally with access to AWS credentials. Cowork calls this
via MCP to execute Athena queries without needing credentials in
the sandbox.

Usage:
    python helpers/mcp_athena_server.py
"""

import json
import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("athena-query")

# Connection config — reads from env or defaults
ATHENA_CONFIG = {
    "database": os.environ.get("ATHENA_DATABASE", "trayaprod"),
    "s3_staging_dir": os.environ.get("ATHENA_S3_STAGING", "s3://traya-dp-prod/athena-output/"),
    "region_name": os.environ.get("ATHENA_REGION", "ap-south-1"),
    "work_group": os.environ.get("ATHENA_WORKGROUP", "jupyter"),
    "profile_name": os.environ.get("AWS_PROFILE", "prod"),
}


def _get_connection():
    """Create a PyAthena connection using local AWS credentials."""
    from pyathena import connect
    import boto3

    session = boto3.Session(profile_name=ATHENA_CONFIG["profile_name"])
    return connect(
        s3_staging_dir=ATHENA_CONFIG["s3_staging_dir"],
        region_name=ATHENA_CONFIG["region_name"],
        work_group=ATHENA_CONFIG["work_group"],
        schema_name=ATHENA_CONFIG["database"],
        boto3_session=session,
    )


@mcp.tool()
def query_athena(sql: str) -> str:
    """Execute a SELECT query against AWS Athena and return results as JSON.

    Args:
        sql: The SQL SELECT query to execute. Use fully qualified table names
             for cross-database queries (e.g., trayaprod.engagements_vw).
             Available databases: trayaprod, tatvav2db_public, traya_marts_ez, google_analytics.
             IMPORTANT: Only SELECT queries are supported. Do not use SHOW, USE, DESCRIBE, or DDL.
             Always include LIMIT to avoid scanning too much data.

    Returns:
        JSON string with columns and rows, or error message.
    """
    try:
        conn = _get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        columns = [desc[0] for desc in cur.description] if cur.description else []
        rows = cur.fetchall()
        cur.close()
        conn.close()

        data = [dict(zip(columns, row)) for row in rows[:500]]
        result = {
            "columns": columns,
            "row_count": len(rows),
            "data": data,
        }
        if len(rows) > 500:
            result["truncated"] = True
            result["total_rows"] = len(rows)

        return json.dumps(result, default=str)

    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def list_athena_tables(database: str = "") -> str:
    """List all tables in an Athena/Glue database.

    Args:
        database: Glue catalog database name. Defaults to trayaprod.
                  Common databases: trayaprod, tatvav2db_public,
                  traya_marts_ez, google_analytics.
    """
    try:
        db = database or ATHENA_CONFIG["database"]
        conn = _get_connection()
        cur = conn.cursor()
        cur.execute(f"SHOW TABLES IN {db}")
        tables = sorted(row[0] for row in cur.fetchall())
        cur.close()
        conn.close()
        return json.dumps({"database": db, "tables": tables, "count": len(tables)})
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def describe_athena_table(table: str, database: str = "") -> str:
    """Get column names and types for a table.

    Args:
        table: Table name (e.g., engagements_vw, orders_vw).
        database: Database name. Defaults to trayaprod.
    """
    try:
        db = database or ATHENA_CONFIG["database"]
        conn = _get_connection()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = '{db}' AND table_name = '{table}'
            ORDER BY ordinal_position
        """)
        columns = [{"name": row[0], "type": row[1]} for row in cur.fetchall()]
        cur.close()
        conn.close()
        return json.dumps({"database": db, "table": table, "columns": columns})
    except Exception as e:
        return json.dumps({"error": str(e)})


if __name__ == "__main__":
    mcp.run()
