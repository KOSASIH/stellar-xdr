# tests/test_pi_value_manager.py

import unittest
from ai_pi_value_setter.pi_value_manager import PiValueManager

class TestPiValueManager(unittest.TestCase):

    def setUp(self):
        self.manager = PiValueManager()

    def test_singleton_instance(self):
        manager2 = PiValueManager()
        self.assertIs(self.manager, manager2, "PiValueManager should be a singleton")

    def test_fixed_value(self):
        self.assertEqual(self.manager.get_value(), 314159, "Fixed Pi value should be 314159")

    def test_validate_value(self):
        self.assertTrue(self.manager.validate_value(314159))
        self.assertFalse(self.manager.validate_value(123456))

    def test_enforce_fixed_value(self):
        class DummyTransaction:
            def __init__(self, value):
                self.value = value

        tx = DummyTransaction(1000)
        updated_tx = self.manager.enforce_fixed_value(tx)
        self.assertEqual(updated_tx.value, 314159)

    def test_update_value_raises(self):
        with self.assertRaises(RuntimeError):
            self.manager.update_value(123456)

    def test_enforce_fixed_value_missing_attr(self):
        class DummyTransaction:
            pass

        tx = DummyTransaction()
        with self.assertRaises(AttributeError):
            self.manager.enforce_fixed_value(tx)

if __name__ == "__main__":
    unittest.main()
