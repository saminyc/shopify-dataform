import duckdb

# Connect with the database
conn = duckdb.connect("database/shopify.duckdb")

print("Tables:")
print(conn.execute("SHOW TABLES").fetchdf())

print("\nProducts:")
print(
    conn.execute("""
        SELECT
            id,
            title,
            vendor,
            product_type
        FROM raw_products
        LIMIT 10
    """).fetchdf()
)

conn.close()