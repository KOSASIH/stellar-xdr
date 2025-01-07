import re

def validate_account_id(account_id: str) -> bool:
    # Implement regex validation for account ID format
    return bool(re.match(r'^[A-Z0-9]{56}$', account_id))  # Example regex for Stellar account IDs

def validate_transaction(transaction) -> bool:
    return (
        validate_account_id(transaction.source.account_id) and
        validate_account_id(transaction.destination.account_id) and
        transaction.amount > 0
    )
