import pytest
from unittest.mock import patch, MagicMock
from dags.extract import extract_product_data
from datetime import datetime

@patch('dags.extract.requests.get')
@patch('dags.extract.os.getenv')
def test_extract_product_data(mock_getenv, mock_get):
    # Mock the API key
    mock_getenv.return_value = "fake_api_key"
    
    # Mock the response of requests.get
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = '''
    <html>
        <span id="productTitle">Test Product</span>
        <span class="a-offscreen">£19.99</span>
        <span class="a-icon-alt">4.5 out of 5 stars</span>
    </html>
    '''.encode("utf-8")
    mock_get.return_value = mock_response
    
    urls = ["https://www.amazon.co.uk/Bulk-Essential-Protein-Powder-Strawberry/dp/B09T1BWCFT"]
    product_data = extract_product_data(urls)
    
    # Assert the API was called with the correct URL
    expected_scraper_url = "http://api.scraperapi.com?api_key=fake_api_key&url=https://www.amazon.co.uk/Bulk-Essential-Protein-Powder-Strawberry/dp/B09T1BWCFT&country_code=uk"
    mock_get.assert_called_with(expected_scraper_url, timeout=10)
    
    # Assert the data structure
    assert len(product_data) == 1
    assert product_data[0]["title"] == "Test Product"
    assert product_data[0]["price"] == "£19.99"
    assert product_data[0]["rating"] == "4.5 out of 5 stars"
    assert product_data[0]["url"] == "https://www.amazon.co.uk/Bulk-Essential-Protein-Powder-Strawberry/dp/B09T1BWCFT"
    assert "scraped_at" in product_data[0]
    assert datetime.fromisoformat(product_data[0]["scraped_at"])  # Check if the datetime is in the correct format