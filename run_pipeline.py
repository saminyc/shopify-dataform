from ingestion.extract_products import extract_products
from ingestion.load_duckdb import load_dataframe

def main():
    print("=" * 50)
    print("SHOPIFY INGESTION PIPELINE")
    print("=" * 50)

    products = extract_products()

    print(f"Products extracted: {len(products)}")
    print(products.head())

    load_dataframe(products, "raw_products")

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()