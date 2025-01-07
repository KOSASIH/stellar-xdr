import requests
from src.constants import PiCoinConfig

class StablecoinManager:
    def __init__(self):
        self.current_supply = PiCoinConfig.SUPPLY
        self.reserve = 0  # Initialize reserve
        self.price_oracle_url = PiCoinConfig.PRICE_ORACLE_URL  # URL for the price oracle API

    def fetch_current_price(self):
        """Fetch the current price of Pi Coin from the price oracle."""
        try:
            response = requests.get(self.price_oracle_url)
            response.raise_for_status()
            price_data = response.json()
            return price_data['price']  # Assuming the API returns a JSON with a 'price' field
        except requests.RequestException as e:
            print(f"Error fetching price: {e}")
            return None

    def adjust_supply(self):
        """Adjust the supply of Pi Coin based on market conditions."""
        current_price = self.fetch_current_price()
        if current_price is None:
            return  # Exit if price fetch failed

        if current_price < PiCoinConfig.VALUE:
            self.increase_supply()
        elif current_price > PiCoinConfig.VALUE:
            self.decrease_supply()

    def increase_supply(self):
        """Increase the supply of Pi Coin."""
        # Logic to mint new coins
        new_coins = self.calculate_mint_amount()
        self.current_supply += new_coins
        self.reserve += new_coins * PiCoinConfig.VALUE  # Update reserve based on the new supply
        print(f"Minted {new_coins} new Pi Coins. New supply: {self.current_supply}")

    def decrease_supply(self):
        """Decrease the supply of Pi Coin."""
        # Logic to burn coins
        coins_to_burn = self.calculate_burn_amount()
        if coins_to_burn > self.current_supply:
            coins_to_burn = self.current_supply  # Can't burn more than current supply
        self.current_supply -= coins_to_burn
        self.reserve -= coins_to_burn * PiCoinConfig.VALUE  # Update reserve based on the burned supply
        print(f"Burned {coins_to_burn} Pi Coins. New supply: {self.current_supply}")

    def calculate_mint_amount(self):
        """Calculate the amount of new coins to mint based on market conditions."""
        # Placeholder logic for minting amount calculation
        return int(self.current_supply * 0.01)  # Mint 1% of current supply

    def calculate_burn_amount(self):
        """Calculate the amount of coins to burn based on market conditions."""
        # Placeholder logic for burning amount calculation
        return int(self.current_supply * 0.01)  # Burn 1% of current supply

    def manage_reserves(self):
        """Manage the reserves backing Pi Coin."""
        # Logic to ensure reserves are sufficient
        if self.reserve < (self.current_supply * PiCoinConfig.VALUE):
            print("Warning: Reserves are insufficient to back the current supply.")
            # Implement additional logic to address this issue (e.g., halt minting)

    def run_stability_mechanism(self):
        """Run the stability mechanism to maintain the peg."""
        self.adjust_supply()
        self.manage_reserves()

if __name__ == "__main__":
    manager = StablecoinManager()
    manager.run_stability_mechanism()
