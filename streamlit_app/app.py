import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DB_URI = os.getenv("DATABASE_URI_OC")
engine = create_engine(DB_URI)

st.title("📊 Amazon Price Tracker")

df = pd.read_sql("SELECT * FROM products", engine)

if df.empty:
    st.write("No data available.")
else:
    st.dataframe(df)

    st.subheader("Filter by Price")
    min_price, max_price = st.slider("Select price range", 0.0, 100.0, (0.0, 100.0))
    filtered_df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

    st.subheader("Filter by Rating")
    min_rating, max_rating = st.slider("Select rating range", 0.0, 5.0, (0.0, 5.0))
    filtered_df = filtered_df[(filtered_df['rating'] >= min_rating) & (filtered_df['rating'] <= max_rating)]

    st.write(f"Showing {len(filtered_df)} products within the selected filters.")

    sort_option = st.selectbox("Sort by", ["Price (Low to High)", "Price (High to Low)", "Rating", "Scraped At"])
    if sort_option == "Price (Low to High)":
        filtered_df = filtered_df.sort_values("price", ascending=True)
    elif sort_option == "Price (High to Low)":
        filtered_df = filtered_df.sort_values("price", ascending=False)
    elif sort_option == "Rating":
        filtered_df = filtered_df.sort_values("rating", ascending=False)
    elif sort_option == "Scraped At":
        filtered_df = filtered_df.sort_values("scraped_at", ascending=False)

    st.dataframe(filtered_df)

    st.subheader("Price Trends Over Time")
    st.line_chart(filtered_df.set_index("scraped_at")["price"])

    st.subheader("Top 5 Most Expensive Products")
    top_expensive = df.nlargest(5, 'price')
    st.dataframe(top_expensive)

    st.subheader("Top 5 Highest Rated Products")
    top_rated = df.nlargest(5, 'rating')
    st.dataframe(top_rated)

    st.subheader("Search for a Product")
    search_query = st.text_input("Enter product name:")
    if search_query:
        search_results = df[df['title'].str.contains(search_query, case=False, na=False)]
        st.write(f"Found {len(search_results)} product(s) matching your search.")
        st.dataframe(search_results)

    st.subheader("Filter by Date")
    min_date = st.date_input("Start Date", value=pd.to_datetime("2025-01-01"))
    max_date = st.date_input("End Date", value=pd.to_datetime("today"))
    date_filtered_df = filtered_df[(filtered_df['scraped_at'] >= str(min_date)) & (filtered_df['scraped_at'] <= str(max_date))]
    st.write(f"Showing {len(date_filtered_df)} products within the selected date range.")
    st.dataframe(date_filtered_df)

    st.subheader("Download Data")
    st.download_button(
        label="Download data as CSV",
        data=date_filtered_df.to_csv(index=False),
        file_name="amazon_price_tracker_data.csv",
        mime="text/csv"
    )

