# examples/run_ai_pi_value_setter.py

"""
Ultra High-Tech Example Usage of the Autonomous Pi Coin AI System

This script demonstrates the full workflow of the AI system managing Pi Coin transactions:
- Creating dummy transactions from various sources
- Processing them through the AutonomousPiAI controller
- Showing how pure Pi Coins get the special badge 🌟
- Rejecting transactions from exchanges or invalid sources
"""

import logging
import sys
from ai_pi_value_setter.autonomous_controller import AutonomousPiAI

# Configure logging to output to console with detailed debug info
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
    stream=sys.stdout
)

def main():
    ai = AutonomousPiAI()

    class DummyPiCoin:
        def __init__(self):
            self.is_pure = False
            self.badge = None

        def __repr__(self):
            return f"<DummyPiCoin is_pure={self.is_pure} badge={self.badge}>"

    class DummyTransaction:
        def __init__(self, source, value=0):
            self.source = source
            self.value = value
            self.pi_coin = DummyPiCoin()

        def __repr__(self):
            return f"<DummyTransaction source={self.source} value={self.value} pi_coin={self.pi_coin}>"

    # Create a list of sample transactions from various sources
    sample_transactions = [
        DummyTransaction("mining", 5000),
        DummyTransaction("p2p", 10000),
        DummyTransaction("contribution", 7500),
        DummyTransaction("exchange", 20000),  # Should be rejected
        DummyTransaction("unknown", 3000),    # Should be rejected
        DummyTransaction("P2P", 15000),       # Case-insensitive valid source
    ]

    print("\n--- Processing Transactions Through AutonomousPiAI ---\n")

    for tx in sample_transactions:
        print(f"Processing transaction: {tx}")
        processed_tx = ai.process_transaction(tx)
        if processed_tx:
            print(f"✅ Accepted: {processed_tx}")
        else:
            print(f"❌ Rejected: {tx}")
        print("-" * 60)

if __name__ == "__main__":
    main()
