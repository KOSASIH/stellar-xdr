# tests/test_badge_assigner.py

import unittest
from ai_pi_value_setter.badge_assigner import BadgeAssigner

class TestBadgeAssigner(unittest.TestCase):

    def setUp(self):
        self.assigner = BadgeAssigner()

    def test_assign_badge_to_pure_coin(self):
        class DummyPiCoin:
            def __init__(self, is_pure):
                self.is_pure = is_pure
                self.badge = None

        pure_coin = DummyPiCoin(True)
        updated_coin = self.assigner.assign_badge(pure_coin)
        self.assertEqual(updated_coin.badge, "🌟")

    def test_remove_badge_from_impure_coin(self):
        class DummyPiCoin:
            def __init__(self, is_pure):
                self.is_pure = is_pure
                self.badge = "🌟"

        impure_coin = DummyPiCoin(False)
        updated_coin = self.assigner.assign_badge(impure_coin)
        self.assertIsNone(updated_coin.badge)

    def test_missing_is_pure_attr_raises(self):
        class DummyPiCoin:
            def __init__(self):
                self.badge = None

        coin = DummyPiCoin()
        with self.assertRaises(AttributeError):
            self.assigner.assign_badge(coin)

if __name__ == "__main__":
    unittest.main()
