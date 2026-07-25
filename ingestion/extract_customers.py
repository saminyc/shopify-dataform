import pandas as pd
from ingestion.shopify_client import get


def extract_customers(limit=250):
    data = get(
        "customers.json",
        params={
            "limit": limit
        }
    )

    return pd.json_normalize(data["customers"])