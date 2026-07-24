from ingestion.extract_products import extract_products

def main():
    print("=" * 50)
    print("SHOPIFY INGESTION PIPELINE")
    print("=" * 50)

    products = extract_products()

    print(f"Products extracted: {len(products)}")
    print(products.head())

if __name__ == "__main__":
    main()