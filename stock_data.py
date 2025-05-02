import yfinance as yf
import time
import random
import pandas as pd

def fetch_stock_data(ticker, max_period='max', max_retries=5, base_delay=1):
    """
    Fetches stock data with retry logic and exponential backoff.
    
    Parameters:
    -----------
    ticker : str
        The stock ticker symbol
    max_period : str, optional
        The maximum period of data to fetch (default is 'max')
    max_retries : int, optional
        Maximum number of retry attempts (default is 5)
    base_delay : int, optional
        Base delay in seconds for exponential backoff (default is 1)
    
    Returns:
    --------
    pandas.Series
        The closing prices for the specified ticker
    """
    for attempt in range(max_retries):
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period=max_period, interval='1d')
            return data['Close']
        except Exception as e:
            if attempt == max_retries - 1:  # Last attempt
                raise e
            
            # Calculate delay with exponential backoff and jitter
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed. Retrying in {delay:.2f} seconds...")
            time.sleep(delay)
    
    raise Exception("Failed to fetch data after maximum retries") 