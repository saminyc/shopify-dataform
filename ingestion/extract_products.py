# ingestion/extract_products.py

import pandas as pd
from ingestion.shopify_client import get


def extract_products(limit=250):

    data = get(
        "products.json",
        params={
            "limit": limit
        }
    )

    return pd.json_normalize(data["products"])