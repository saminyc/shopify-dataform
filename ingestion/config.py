from dotenv import load_dotenv
import os

load_dotenv()

SHOP_NAME = os.getenv("SHOP_NAME")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_VERSION = os.getenv("API_VERSION")

BASE_URL = (
    f"https://{SHOP_NAME}.myshopify.com/admin/api/"
    f"{API_VERSION}"
)