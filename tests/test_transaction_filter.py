# tests/test_transaction_filter.py

import unittest
from ai_pi_value_setter.transaction_filter import TransactionFilter

class TestTransactionFilter(unittest.TestCase):

    def setUp(self):
        self.filter = TransactionFilter()

    def test_valid_sources(self):
        class DummyTransaction:
            def __init__(self, source):
                self.source = source

        valid_sources = ['mining', 'p2p', 'contribution', 'P2P', 'Mining']
        for source in valid_sources:
            tx = DummyTransaction(source)
            self.assertTrue(self.filter.is_valid_transaction(tx), f"Source '{source}' should be valid")

    def test_invalid_sources(self):
        class DummyTransaction:
            def __init__(self, source):
                self.source = source

        invalid_sources = ['exchange', 'unknown', '', 'marketplace']
        for source in invalid_sources:
            tx = DummyTransaction(source)
            self.assertFalse(self.filter.is_valid_transaction(tx), f"Source '{source}' should be invalid")

    def test_filter_transactions(self):
        class DummyTransaction:
            def __init__(self, source):
                self.source = source

        txs = [
            DummyTransaction('mining'),
            DummyTransaction('exchange'),
            DummyTransaction('p2p'),
            DummyTransaction('unknown'),
            DummyTransaction('contribution'),
        ]
        filtered = self.filter.filter_transactions(txs)
        self.assertEqual(len(filtered), 3)
        self.assertTrue(all(tx.source.lower() in {'mining', 'p2p', 'contribution'} for tx in filtered))

    def test_missing_source_attr_raises(self):
        class DummyTransaction:
            pass

        tx = DummyTransaction()
        with self.assertRaises(AttributeError):
            self.filter.is_valid_transaction(tx)

if __name__ == "__main__":
    unittest.main()
