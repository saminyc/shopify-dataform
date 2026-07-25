# ingestion/shopify_client.py

import requests
from ingestion.config import BASE_URL, ACCESS_TOKEN

HEADERS = {
    "X-Shopify-Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json",
}


def get(endpoint: str, params=None):
    url = f"{BASE_URL}/{endpoint}"

    response = requests.get(
        url,
        headers=HEADERS,
        params=params
    )

    response.raise_for_status()

    return response.json()