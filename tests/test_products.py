from ingestion.extract_products import extract_products

df = extract_products()

print(df.head())
print(df.shape)