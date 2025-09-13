# ai_pi_value_setter/transaction_filter.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class TransactionFilter:
    """
    TransactionFilter validates transactions to ensure only those originating from
    mining, peer-to-peer (P2P), or contribution sources are accepted into the Pi Network ecosystem.
    Transactions originating from exchanges or other unauthorized sources are rejected.
    """

    # Allowed sources for valid Pi Coin transactions
    ALLOWED_SOURCES = {'mining', 'p2p', 'contribution'}

    def __init__(self):
        logger.info("TransactionFilter initialized with allowed sources: %s", self.ALLOWED_SOURCES)

    def is_valid_transaction(self, transaction):
        """
        Validates if the transaction source is allowed.

        Args:
            transaction (object): Transaction object expected to have a 'source' attribute (string).

        Returns:
            bool: True if transaction source is allowed, False otherwise.
        """
        if not hasattr(transaction, 'source'):
            logger.error("Transaction object missing 'source' attribute")
            raise AttributeError("Transaction object must have a 'source' attribute")

        source = transaction.source.lower()
        is_valid = source in self.ALLOWED_SOURCES

        if is_valid:
            logger.debug(f"Transaction from source '{source}' is valid.")
        else:
            logger.warning(f"Transaction from source '{source}' is invalid and rejected.")

        return is_valid

    def filter_transactions(self, transactions):
        """
        Filters a list (or iterable) of transactions, returning only valid ones.

        Args:
            transactions (iterable): Iterable of transaction objects.

        Returns:
            list: List of valid transaction objects.
        """
        valid_txs = []
        for tx in transactions:
            try:
                if self.is_valid_transaction(tx):
                    valid_txs.append(tx)
            except Exception as e:
                logger.error(f"Error validating transaction: {e}")
        logger.info(f"Filtered {len(valid_txs)} valid transactions out of {len(transactions)} total.")
        return valid_txs

# Internal test example
if __name__ == "__main__":
    class DummyTransaction:
        def __init__(self, source):
            self.source = source

        def __repr__(self):
            return f"<DummyTransaction source={self.source}>"

    filterer = TransactionFilter()

    test_transactions = [
        DummyTransaction("mining"),
        DummyTransaction("p2p"),
        DummyTransaction("contribution"),
        DummyTransaction("exchange"),
        DummyTransaction("unknown"),
        DummyTransaction("P2P"),  # test case-insensitivity
    ]

    print("Testing individual transaction validation:")
    for tx in test_transactions:
        result = filterer.is_valid_transaction(tx)
        print(f"Transaction {tx} valid? {result}")

    print("\nTesting batch filtering:")
    valid_transactions = filterer.filter_transactions(test_transactions)
    print(f"Valid transactions: {valid_transactions}")
