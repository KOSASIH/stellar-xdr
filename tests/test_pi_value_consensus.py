# tests/test_pi_value_consensus.py

import unittest
from ai_pi_value_setter.pi_value_consensus import PiValueConsensusEnforcer
from ai_pi_value_setter.config import Config

class DummyPiCoin:
    def __init__(self, is_pure=True):
        self.is_pure = is_pure
        self.badge = None

    def __repr__(self):
        return f"<DummyPiCoin is_pure={self.is_pure} badge={self.badge}>"

class DummyTransaction:
    def __init__(self, source, value, is_pure=True):
        self.source = source
        self.value = value
        self.pi_coin = DummyPiCoin(is_pure)

    def __repr__(self):
        return f"<DummyTransaction source={self.source} value={self.value} pi_coin={self.pi_coin}>"

class TestPiValueConsensusEnforcer(unittest.TestCase):

    def setUp(self):
        self.enforcer = PiValueConsensusEnforcer()
        self.fixed_value = Config.FIXED_PI_VALUE

    def test_accept_valid_transaction(self):
        tx = DummyTransaction(source="mining", value=self.fixed_value, is_pure=True)
        self.assertTrue(self.enforcer.is_transaction_accepted(tx))

    def test_reject_transaction_from_exchange(self):
        tx = DummyTransaction(source="exchange", value=self.fixed_value, is_pure=True)
        self.assertFalse(self.enforcer.is_transaction_accepted(tx))

    def test_reject_transaction_invalid_source(self):
        tx = DummyTransaction(source="unknown_source", value=self.fixed_value, is_pure=True)
        self.assertFalse(self.enforcer.is_transaction_accepted(tx))

    def test_reject_transaction_wrong_value(self):
        tx = DummyTransaction(source="mining", value=123456, is_pure=True)
        self.assertFalse(self.enforcer.is_transaction_accepted(tx))

    def test_reject_transaction_impure_coin(self):
        tx = DummyTransaction(source="mining", value=self.fixed_value, is_pure=False)
        self.assertFalse(self.enforcer.is_transaction_accepted(tx))

    def test_reject_transaction_missing_attributes(self):
        class IncompleteTransaction:
            pass

        tx = IncompleteTransaction()
        self.assertFalse(self.enforcer.is_transaction_accepted(tx))

    def test_filter_accepted_transactions(self):
        txs = [
            DummyTransaction("mining", self.fixed_value, True),
            DummyTransaction("exchange", self.fixed_value, True),
            DummyTransaction("p2p", self.fixed_value, True),
            DummyTransaction("mining", 123, True),
            DummyTransaction("contribution", self.fixed_value, False),
        ]
        accepted = list(self.enforcer.filter_accepted_transactions(txs))
        self.assertEqual(len(accepted), 2)
        for tx in accepted:
            self.assertTrue(self.enforcer.is_transaction_accepted(tx))

if __name__ == "__main__":
    unittest.main()
