from ingestion.extract_products import extract_products
from ingestion.extract_customers import extract_customers
from ingestion.extract_orders import extract_orders
from ingestion.load_duckdb import load_dataframe


def main():
    print("=" * 60)
    print("SHOPIFY ANALYTICS EL PIPELINE")
    print("=" * 60)

    jobs = [
        ("products", extract_products),
        ("customers", extract_customers),
        ("orders", extract_orders),
    ]

    for table_name, extractor in jobs:

        print(f"\nExtracting {table_name}...")

        df = extractor()

        print(f"✓ Extracted {len(df)} rows")

        load_dataframe(df, f"raw_{table_name}")

    print("\n🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()