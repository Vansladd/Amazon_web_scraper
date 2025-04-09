import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os

def extract_product_data(urls):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    product_data = []

    for url in urls:
        scraper_url = f"http://api.scraperapi.com?api_key={api_key}&url={url}&country_code=uk"
        print("Starting request for:", url)
        
        try:
            response = requests.get(scraper_url, timeout=10)
            response.raise_for_status() 
            print("Request completed with status code:", response.status_code)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                title_tag = soup.find("span", {"id": "productTitle"})
                price_tag = soup.find("span", {"class": "a-offscreen"})
                rating_tag = soup.find("span", {"class": "a-icon-alt"})

                title = title_tag.get_text(strip=True) if title_tag else "N/A"
                price = price_tag.get_text(strip=True) if price_tag else "N/A"
                rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"

                product_data.append({
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "url": url,
                    "scraped_at": datetime.now().isoformat()
                })
            else:
                print(f"Error: {response.status_code} for URL {url}")
        
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred for {url}: {err}")
        except Exception as err:
            print(f"Other error occurred for {url}: {err}")

    return product_data