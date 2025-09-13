# ai_pi_value_setter/pi_value_consensus.py

import logging
from typing import Any, Iterable

from .config import Config
from .exchange_detector import ExchangeDetector
from .transaction_filter import TransactionFilter
from .pi_value_manager import PiValueManager

logger = logging.getLogger(__name__)
logger.setLevel(Config.LOG_LEVEL)

class PiValueConsensusEnforcer:
    """
    Ensures the entire Pi Network ecosystem enforces and agrees on the fixed Pi Coin value ($314,159).
    This class acts as a gatekeeper for all transactions entering the ecosystem,
    guaranteeing only pure Pi Coins with the fixed value are accepted.
    """

    def __init__(self):
        self.value_manager = PiValueManager()
        self.tx_filter = TransactionFilter()
        self.exchange_detector = ExchangeDetector()
        logger.info("PiValueConsensusEnforcer initialized.")

    def is_transaction_accepted(self, transaction: Any) -> bool:
        """
        Validates a single transaction against all ecosystem rules:
        - Reject if from exchange or blacklisted source
        - Reject if source is invalid
        - Reject if Pi Coin value is not fixed
        - Reject if Pi Coin is not pure (has been on exchange or tampered)

        Args:
            transaction (Any): Transaction object with attributes:
                - source (str)
                - value (int)
                - pi_coin (object) with attribute is_pure (bool)

        Returns:
            bool: True if transaction is accepted by ecosystem, False otherwise.
        """
        try:
            if self.exchange_detector.is_from_exchange(transaction):
                logger.warning(f"Rejected transaction from exchange source: {transaction.source}")
                return False

            if not self.tx_filter.is_valid_transaction(transaction):
                logger.warning(f"Rejected transaction from invalid source: {transaction.source}")
                return False

            if not hasattr(transaction, "value") or transaction.value != self.value_manager.value:
                logger.warning(f"Rejected transaction with invalid Pi Coin value: {getattr(transaction, 'value', None)}")
                return False

            if not hasattr(transaction, "pi_coin") or not getattr(transaction.pi_coin, "is_pure", False):
                logger.warning("Rejected transaction with impure Pi Coin")
                return False

            logger.debug("Transaction accepted by PiValueConsensusEnforcer")
            return True

        except Exception as e:
            logger.error(f"Error during transaction validation: {e}")
            return False

    def filter_accepted_transactions(self, transactions: Iterable[Any]) -> Iterable[Any]:
        """
        Filters a batch of transactions, returning only those accepted by the ecosystem.

        Args:
            transactions (Iterable[Any]): Iterable of transaction objects.

        Returns:
            Iterable[Any]: Filtered iterable of accepted transactions.
        """
        accepted = []
        for tx in transactions:
            if self.is_transaction_accepted(tx):
                accepted.append(tx)
            else:
                logger.debug(f"Transaction rejected in batch filtering: {tx}")
        logger.info(f"Filtered {len(accepted)} accepted transactions out of {len(list(transactions))}")
        return accepted
