from unittest.mock import patch, MagicMock
import pytest
import pandas as pd
from dags.load import load_to_db

@patch('dags.load.create_engine')
@patch('pandas.DataFrame.to_sql')
@patch('dags.load.os.getenv')
def test_load_to_db(mock_getenv, mock_to_sql, mock_create_engine):
    # Mock env var
    mock_getenv.return_value = "postgresql://user:password@localhost:5432/testdb"
    
    # Mock engine and connection
    mock_connection = MagicMock()
    mock_engine = MagicMock()
    mock_connection.execute = MagicMock()
    mock_engine.connect.return_value.__enter__.return_value = mock_connection
    mock_create_engine.return_value = mock_engine
    
    # Sample DataFrame
    df = pd.DataFrame({
        "title": ["Test Product"],
        "price": ["19.99"],
        "rating": ["4.5"],
        "url": ["https://example.com"],
        "scraped_at": [pd.to_datetime("2025-04-10")]
    })
    
    # Run
    load_to_db(df)
    
    # Assertions
    mock_getenv.assert_called_with("DATABASE_URI")
    mock_create_engine.assert_called_once()
    mock_connection.execute.assert_called_once()
    mock_to_sql.assert_called_once_with("products", mock_engine, if_exists="append", index=False)
