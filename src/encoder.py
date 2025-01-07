from .xdr_types import AccountID, Transaction

def encode_batch(transactions: List[Transaction]) -> bytes:
    encoded_data = b''.join(tx.to_xdr() for tx in transactions)
    return encoded_data
