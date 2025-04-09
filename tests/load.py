from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

# Function to load data to PostgreSQL
def load_to_db(df):
    load_dotenv()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        price NUMERIC,
        rating FLOAT,
        url VARCHAR(255),
        scraped_at TIMESTAMP
    );
    """
    DB_URI = os.getenv("DATABASE_URI")
    engine = create_engine(DB_URI)
    try:
        with engine.connect() as connection:
            connection.execute(create_table_sql)
        df.to_sql("products", engine, if_exists="append", index=False)
        print(f"Successfully inserted {len(df)} rows.")
    except Exception as e:
        print(f"Error inserting data: {e}")


        
