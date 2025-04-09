from extract import extract_product_data
from transform import transform_data
from load import load_to_db
from dotenv import load_dotenv
import os

def run_etl():
    load_dotenv()
    urls = os.getenv("PRODUCT_URLS","").split(",")
    raw_data = extract_product_data(urls)
    transformed_data = transform_data(raw_data)
    load_to_db(transformed_data)


if __name__ == "__main__":
    run_etl()