# API Reference

This section provides a detailed reference for the classes and functions in the Stellar XDR library.

## Classes

### `AccountID`

Represents a Stellar account ID.

#### Methods

- `__init__(account_id: str)`: Initializes an AccountID instance.
- `is_valid_account_id(account_id: str) -> bool`: Validates the format of the account ID.
- `to_xdr() -> bytes`: Converts the account ID to XDR format.
- `from_xdr(xdr_data: bytes) -> AccountID`: Creates an AccountID from XDR data.

### `Transaction`

Represents a Stellar transaction.

#### Methods

- `__init__(source: AccountID, destination: AccountID, amount: float)`: Initializes a Transaction instance.
- `to_xdr() -> bytes`: Converts the transaction to XDR format.
- `from_xdr(xdr_data: bytes) -> Transaction`: Creates a Transaction from XDR data.

## Functions

### `encode_batch(transactions: List[Transaction]) -> bytes`

Encodes a list of transactions into XDR format.

### `decode_batch(xdr_data: bytes) -> List ```markdown
[Transaction]`

Decodes XDR data into a list of Transaction objects.

### `sign_transaction(transaction_data: bytes, private_key: str) -> bytes`

Signs a transaction using the provided private key.

### `verify_signature(transaction_data: bytes, signature: bytes, public_key: str) -> bool`

Verifies the signature of a transaction using the corresponding public key.

## Error Handling

The library raises exceptions for various error conditions, such as invalid account IDs or failed signature verifications. Ensure to handle these exceptions in your application to maintain robustness.

## Conclusion

This API reference provides a comprehensive overview of the Stellar XDR library's capabilities. For further assistance, please refer to the [Usage](usage.md) section or reach out to the community.
