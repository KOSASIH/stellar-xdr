# ai_pi_value_setter/config.py

import os

class Config:
    """
    Centralized configuration for AI Pi Value Setter system.
    Supports environment variable overrides.
    """

    FIXED_PI_VALUE = int(os.getenv("FIXED_PI_VALUE", "314159"))
    ALLOWED_SOURCES = {"mining", "p2p", "contribution"}
    BLACKLISTED_SOURCES = {"exchange", "centralized_exchange", "dex", "marketplace"}
    BADGE_SYMBOL = os.getenv("BADGE_SYMBOL", "🌟")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
    STELLAR_NETWORK_URL = os.getenv("STELLAR_NETWORK_URL", "https://horizon.stellar.org")
