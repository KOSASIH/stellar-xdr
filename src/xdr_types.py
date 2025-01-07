import struct
from typing import List

class AccountID:
    def __init__(self, account_id: str):
        if not self.is_valid_account_id(account_id):
            raise ValueError("Invalid account ID format.")
        self.account_id = account_id

    @staticmethod
    def is_valid_account_id(account_id: str) -> bool:
        # Implement validation logic (e.g., length, format)
        return len(account_id) == 56  # Example length check

    def to_xdr(self) -> bytes:
        # Convert the account ID to XDR format
        return struct.pack('!56s', self.account_id.encode('utf-8'))

    @staticmethod
    def from_xdr(xdr_data: bytes) -> 'AccountID':
        account_id = struct.unpack('!56s', xdr_data)[0].decode('utf-8').strip('\x00')
        return AccountID(account_id)

class Transaction:
    def __init__(self, source: AccountID, destination: AccountID, amount: float):
        self.source = source
        self.destination = destination
        self.amount = amount

    def to_xdr(self) -> bytes:
        # Serialize transaction to XDR
        return self.source.to_xdr() + self.destination.to_xdr() + struct.pack('!d', self.amount)

    @staticmethod
    def from_xdr(xdr_data: bytes) -> 'Transaction':
        source = AccountID.from_xdr(xdr_data[:56])
        destination = AccountID.from_xdr(xdr_data[56:112])
        amount = struct.unpack('!d', xdr_data[112:120])[0]
        return Transaction(source, destination, amount)
