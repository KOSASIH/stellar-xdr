import requests
import time
from src.constants import PiCoinConfig

class PriceOracle:
    def __init__(self):
        self.price_sources = PiCoinConfig.PRICE_ORACLE_URLS  # List of price oracle URLs
        self.cache = {}
        self.cache_expiry = 60  # Cache expiry time in seconds

    def fetch_price_from_source(self, url):
        """Fetch the price from a single price source."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            price_data = response.json()
            return price_data['price']  # Assuming the API returns a JSON with a 'price' field
        except requests.RequestException as e:
            print(f"Error fetching price from {url}: {e}")
            return None

    def get_current_price(self):
        """Get the current price of Pi Coin, using cached value if available."""
        current_time = time.time()
        
        # Check if we have a cached price and if it's still valid
        if 'price' in self.cache and (current_time - self.cache['timestamp'] < self.cache_expiry):
            print("Using cached price.")
            return self.cache['price']

        # Fetch price from available sources
        for url in self.price_sources:
            price = self.fetch_price_from_source(url)
            if price is not None:
                # Cache the fetched price
                self.cache['price'] = price
                self.cache['timestamp'] = current_time
                print(f"Fetched price from {url}: {price}")
                return price

        print("Failed to fetch price from all sources.")
        return None

if __name__ == "__main__":
    oracle = PriceOracle()
    price = oracle.get_current_price()
    if price is not None:
        print(f"Current price of Pi Coin: {price}")
