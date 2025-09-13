# ai_pi_value_setter/exchange_detector.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class ExchangeDetector:
    """
    ExchangeDetector identifies Pi Coin transactions originating from exchanges.
    Transactions from exchanges are automatically rejected from entering the Pi Network ecosystem.
    """

    # List of blacklisted sources representing exchanges
    BLACKLISTED_SOURCES = {'exchange', 'centralized_exchange', 'dex', 'marketplace'}

    def __init__(self):
        logger.info(f"ExchangeDetector initialized with blacklisted sources: {self.BLACKLISTED_SOURCES}")

    def is_from_exchange(self, transaction):
        """
        Checks if the transaction originates from an exchange.

        Args:
            transaction (object): Transaction object expected to have a 'source' attribute (string).

        Returns:
            bool: True if transaction source is blacklisted (exchange), False otherwise.
        """
        if not hasattr(transaction, 'source'):
            logger.error("Transaction object missing 'source' attribute")
            raise AttributeError("Transaction object must have a 'source' attribute")

        source = transaction.source.lower()
        is_blacklisted = source in self.BLACKLISTED_SOURCES

        if is_blacklisted:
            logger.warning(f"Transaction from blacklisted exchange source '{source}' detected and rejected.")
        else:
            logger.debug(f"Transaction source '{source}' is not blacklisted.")

        return is_blacklisted

# Internal test example
if __name__ == "__main__":
    class DummyTransaction:
        def __init__(self, source):
            self.source = source

        def __repr__(self):
            return f"<DummyTransaction source={self.source}>"

    detector = ExchangeDetector()

    test_transactions = [
        DummyTransaction("exchange"),
        DummyTransaction("centralized_exchange"),
        DummyTransaction("dex"),
        DummyTransaction("marketplace"),
        DummyTransaction("mining"),
        DummyTransaction("p2p"),
        DummyTransaction("contribution"),
        DummyTransaction("unknown"),
    ]

    print("Testing exchange detection:")
    for tx in test_transactions:
        result = detector.is_from_exchange(tx)
        print(f"Transaction {tx} from exchange? {result}")
