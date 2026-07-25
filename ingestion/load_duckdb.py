import duckdb
import pandas as pd
from pathlib import Path

DATABASE_DIR = Path("database")
DATABASE_DIR.mkdir(exist_ok=True)

DB_PATH = DATABASE_DIR / "shopify.duckdb"


def load_dataframe(df: pd.DataFrame, table_name: str):
    """
    Load a DataFrame into DuckDB.
    Skip loading if the DataFrame has no columns.
    """

    if df.empty and len(df.columns) == 0:
        print(f"⚠️ Skipping {table_name}: no data returned.")
        return

    conn = duckdb.connect(DB_PATH)

    conn.register("temp_df", df)

    conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM temp_df
    """)

    conn.close()

    print(f"✅ Loaded {len(df)} rows into {table_name}")