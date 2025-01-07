from .xdr_types import Transaction

def decode_batch(xdr_data: bytes) -> List[Transaction]:
    transactions = []
    offset = 0
    while offset < len(xdr_data):
        tx = Transaction.from_xdr(xdr_data[offset:offset + 120])  # Assuming fixed size for simplicity
        transactions.append(tx)
        offset += 120
    return transactions
