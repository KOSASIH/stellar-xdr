# tests/test_exchange_detector.py

import unittest
from ai_pi_value_setter.exchange_detector import ExchangeDetector

class TestExchangeDetector(unittest.TestCase):

    def setUp(self):
        self.detector = ExchangeDetector()

    def test_detect_exchange_sources(self):
        class DummyTransaction:
            def __init__(self, source):
                self.source = source

        blacklisted = ['exchange', 'centralized_exchange', 'dex', 'marketplace']
        for source in blacklisted:
            tx = DummyTransaction(source)
            self.assertTrue(self.detector.is_from_exchange(tx), f"Source '{source}' should be detected as exchange")

    def test_non_exchange_sources(self):
        class DummyTransaction:
            def __init__(self, source):
                self.source = source

        allowed = ['mining', 'p2p', 'contribution', 'unknown']
        for source in allowed:
            tx = DummyTransaction(source)
            self.assertFalse(self.detector.is_from_exchange(tx), f"Source '{source}' should not be detected as exchange")

    def test_missing_source_attr_raises(self):
        class DummyTransaction:
            pass

        tx = DummyTransaction()
        with self.assertRaises(AttributeError):
            self.detector.is_from_exchange(tx)

if __name__ == "__main__":
    unittest.main()
