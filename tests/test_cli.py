# tests/test_cli.py

import unittest
import asyncio
from ai_pi_value_setter.cli import CLI

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

class TestCLI(unittest.IsolatedAsyncioTestCase):

    async def test_process_transactions(self):
        cli = CLI()
        transactions = [
            DummyTransaction("mining", 1000),
            DummyTransaction("exchange", 2000),
            DummyTransaction("p2p", 3000),
        ]
        # Run the async method and ensure no exceptions occur
        await cli.process_transactions(transactions)

if __name__ == "__main__":
    unittest.main()
