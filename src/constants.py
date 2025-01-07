"""
Pi Coin Configuration Constants
This module contains constants related to the Pi Coin cryptocurrency, designed as a stablecoin.
"""

from typing import List

class PiCoinConfig:
    """Configuration constants for Pi Coin as a stablecoin."""

    # General Constants
    SYMBOL: str = "Pi"  # Symbol for Pi Coin
    VALUE: float = 314159.0  # Fixed value of Pi Coin in USD
    SUPPLY: int = 100_000_000_000  # Total supply of Pi Coin
    DECIMALS: int = 18  # Number of decimal places for Pi Coin

    # Transaction Constants
    TRANSACTION_FEE: float = 0.01  # Transaction fee in USD
    MAX_TRANSACTION_SIZE: int = 1_000_000  # Maximum transaction size in bytes

    # Block Constants
    BLOCK_TIME: int = 10  # Average block time in seconds
    GENESIS_BLOCK_TIMESTAMP: str = "2025-01-01T00:00:00Z"  # Timestamp of the genesis block

    # Mining Constants
    MINING_DIFFICULTY: int = 1000  # Difficulty level for mining Pi Coin
    MINING_REWARD: float = 0.0  # Reward for mining a block (set to 0 for stablecoin)

    # Network Constants
    NETWORK_PROTOCOL: str = "PoS"  # Proof of Stake
    MAX_PEERS: int = 100  # Maximum number of peers in the network
    NODE_TIMEOUT: int = 30  # Timeout for node responses in seconds
    CONNECTION_RETRY_INTERVAL: int = 5  # Retry interval for node connections in seconds

    # Staking Constants
    MIN_STAKE_AMOUNT: float = 100.0  # Minimum amount required to stake
    STAKE_REWARD_RATE: float = 0.05  # Annual reward rate for staking

    # API Rate Limits
    API_REQUEST_LIMIT: int = 1000  # Maximum API requests per hour
    API_KEY_EXPIRATION: int = 3600  # API key expiration time in seconds

    # Regulatory Compliance
    KYC_REQUIRED: bool = True  # Whether KYC is required for transactions
    COMPLIANCE_JURISDICTIONS: List[str] = ["US", "EU", "UK"]  # Jurisdictions for compliance

    # Security Features
    ENCRYPTION_ALGORITHM: str = "AES-256"  # Encryption algorithm for securing transactions
    HASHING_ALGORITHM: str = "SHA-256"  # Hashing algorithm for block verification
    SIGNATURE_SCHEME: str = "ECDSA"  # Digital signature scheme for transaction signing

    # Reserve Management
    RESERVE_RATIO: float = 1.0  # Ratio of reserves to total supply (1.0 for full backing)
    RESERVE_CURRENCY: str = "USD"  # Currency to which Pi Coin is pegged
    RESERVE_AUDIT_FREQUENCY: str = "monthly"  # Frequency of reserve audits

    # Stability Mechanisms
    STABILITY_FUND: float = 10_000_000  # Fund to stabilize the price of Pi Coin
    BUYBACK_THRESHOLD: float = 0.95  # Price threshold for buyback operations

    # Price Oracle
    PRICE_ORACLE_URLS: List[str] = [
        "https://api.example.com/price",  # Replace with actual price API URLs
        "https://api.anotherexample.com/price"
    ]

    # Governance Model
    GOVERNANCE_MODEL: str = "Decentralized"  # Governance model for Pi Coin

    # Notification Settings
    NOTIFICATION_CHANNELS: List[str] = ["email", "sms"]  # Supported notification channels

    # Additional constants can be added here as needed
