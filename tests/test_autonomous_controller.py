# tests/test_autonomous_controller.py

import unittest
from ai_pi_value_setter.autonomous_controller import AutonomousPiAI

class TestAutonomousPiAI(unittest.TestCase):

    def setUp(self):
        self.ai = AutonomousPiAI()

    def test_process_valid_transaction(self):
        class DummyPiCoin:
            def __init__(self):
                self.is_pure = False
                self.badge = None

        class DummyTransaction:
            def __init__(self, source, value=0):
                self.source = source
                self.value = value
                self.pi_coin = DummyPiCoin()

        tx = DummyTransaction('mining', 1000)
        processed = self.ai.process_transaction(tx)
        self.assertIsNotNone(processed)
        self.assertEqual(processed.value, 314159)
        self.assertTrue(processed.pi_coin.is_pure)
        self.assertEqual(processed.pi_coin.badge, "🌟")

    def test_reject_exchange_transaction(self):
        class DummyPiCoin:
            def __init__(self):
                self.is_pure = False
                self.badge = None

        class DummyTransaction:
            def __init__(self, source, value=0):
                self.source = source
                self.value = value
                self.pi_coin = DummyPiCoin()

        tx = DummyTransaction('exchange', 1000)
        processed = self.ai.process_transaction(tx)
        self.assertIsNone(processed)

    def test_reject_invalid_source_transaction(self):
        class DummyPiCoin:
            def __init__(self):
                self.is_pure = False
                self.badge = None

        class DummyTransaction:
            def __init__(self, source, value=0):
                self.source = source
                self.value = value
                self.pi_coin = DummyPiCoin()

        tx = DummyTransaction('unknown', 1000)
        processed = self.ai.process_transaction(tx)
        self.assertIsNone(processed)

    def test_missing_pi_coin_attribute(self):
        class DummyTransaction:
            def __init__(self, source, value=0):
                self.source = source
                self.value = value
                # no pi_coin attribute

        tx = DummyTransaction('mining', 1000)
        processed = self.ai.process_transaction(tx)
        self.assertIsNone(processed)

if __name__ == "__main__":
    unittest.main()
