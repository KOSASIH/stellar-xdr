# ai_pi_value_setter/cli.py

import asyncio
import logging
import sys
from typing import List
from ai_pi_value_setter.autonomous_controller import AutonomousPiAI

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

class CLI:
    """
    CLI for AI Pi Value Setter system.
    """

    def __init__(self):
        self.ai = AutonomousPiAI()

    async def process_transactions(self, transactions: List[Any]) -> None:
        for tx in transactions:
            result = await self.ai.process_transaction(tx)
            if result:
                logger.info(f"Transaction accepted: {result}")
            else:
                logger.info(f"Transaction rejected: {tx}")

def main():
    # Example dummy transactions for CLI demo
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

    transactions = [
        DummyTransaction("mining", 1000),
        DummyTransaction("exchange", 2000),
        DummyTransaction("p2p", 3000),
    ]

    cli = CLI()
    asyncio.run(cli.process_transactions(transactions))

if __name__ == "__main__":
    main()
