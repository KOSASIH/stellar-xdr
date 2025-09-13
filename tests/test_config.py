# tests/test_config.py

import unittest
import os
from ai_pi_value_setter import config

class TestConfig(unittest.TestCase):

    def test_default_values(self):
        self.assertEqual(config.Config.FIXED_PI_VALUE, 314159)
        self.assertIn("mining", config.Config.ALLOWED_SOURCES)
        self.assertIn("exchange", config.Config.BLACKLISTED_SOURCES)
        self.assertEqual(config.Config.BADGE_SYMBOL, "🌟")
        self.assertEqual(config.Config.LOG_LEVEL, "DEBUG")
        self.assertTrue(config.Config.STELLAR_NETWORK_URL.startswith("http"))

    def test_env_override(self):
        os.environ["FIXED_PI_VALUE"] = "123456"
        os.environ["BADGE_SYMBOL"] = "⭐"
        # Reload config module to pick up env vars
        import importlib
        importlib.reload(config)
        self.assertEqual(config.Config.FIXED_PI_VALUE, 123456)
        self.assertEqual(config.Config.BADGE_SYMBOL, "⭐")
        # Clean up env vars
        del os.environ["FIXED_PI_VALUE"]
        del os.environ["BADGE_SYMBOL"]

if __name__ == "__main__":
    unittest.main()
