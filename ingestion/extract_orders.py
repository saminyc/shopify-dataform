import pandas as pd
from ingestion.shopify_client import get


def extract_orders(limit=250):
    data = get(
        "orders.json",
        params={
            "status": "any",
            "limit": limit
        }
    )

    return pd.json_normalize(data["orders"])