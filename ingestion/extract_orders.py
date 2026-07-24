import requests
import pandas as pd
from ingestion.config import *


headers = {
    "X-Shopify-Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json",
}

def get_orders():

    url = f"{BASE_URL}/orders.json"

    response = requests.get(
        url,
        headers=headers,
        params={
            "status": "any",
            "limit": 250
        }
    )

    response.raise_for_status()

    data = response.json()["orders"]

    return pd.json_normalize(data)