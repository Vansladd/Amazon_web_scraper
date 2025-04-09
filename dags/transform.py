import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)

    df["price"] = df["price"].str.replace("£","").astype(float)

    df["rating"] = df["rating"].str.split(" ").str[0].astype(float)

    df['scraped_at'] = pd.to_datetime(df['scraped_at'])
    
    return df