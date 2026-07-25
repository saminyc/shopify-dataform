import duckdb

conn = duckdb.connect("database/shopify.duckdb")

for table in ["raw_products", "raw_customers", "raw_orders"]:
    print(f"\n{'=' * 20} {table} {'=' * 20}")
    result = conn.execute(f"DESCRIBE {table}").fetchall()

    for row in result:
        print(f"{row[0]:35} {row[1]}")

conn.close()