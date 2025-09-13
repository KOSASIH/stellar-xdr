# ai_pi_value_setter/config.py

import os
from typing import Final

class Config:
    """
    Configuration class for AI Pi Value Setter system.
    Supports environment variable overrides.
    """

    # Fixed Pi Coin value enforced by the system
    FIXED_PI_VALUE: Final[int] = int(os.getenv("FIXED_PI_VALUE", "314159"))

    # Allowed transaction sources
    ALLOWED_SOURCES: Final[set[str]] = {"mining", "p2p", "contribution"}

    # Blacklisted exchange sources
    BLACKLISTED_SOURCES: Final[set[str]] = {"exchange", "centralized_exchange", "dex", "marketplace"}

    # Badge symbol for pure Pi Coins
    BADGE_SYMBOL: Final[str] = os.getenv("BADGE_SYMBOL", "🌟")

    # Logging level
    LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "DEBUG")

    # Stellar network endpoint (placeholder)
    STELLAR_NETWORK_URL: Final[str] = os.getenv("STELLAR_NETWORK_URL", "https://horizon.stellar.org")

    # Other configs can be added here
