from pathlib import Path
import duckdb
import pandas as pd

DATABASE_DIR = Path("database")
DATABASE_DIR.mkdir(exist_ok=True)

DB_PATH = DATABASE_DIR / "shopify.duckdb"


def load_dataframe(df: pd.DataFrame, table_name: str):
    """
    Loads a pandas DataFrame into DuckDB.
    Replaces the table if it already exists.
    """

    conn = duckdb.connect(DB_PATH)

    conn.register("temp_df", df)

    conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM temp_df
    """)

    conn.close()

    print(f"✅ Loaded {len(df)} rows into {table_name}")