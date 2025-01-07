import unittest
from src.decoder import decode_batch
from src.xdr_types import Transaction, AccountID

class TestDecoder(unittest.TestCase):
    def test_decode_single_transaction(self):
        source = AccountID("GABCDEF12345678901234567890123456789012345678901234567890123456")
        destination = AccountID("GXYZABC12345678901234567890123456789012345678901234567890123456")
        transaction = Transaction(source, destination, 100.0)
        encoded = transaction.to_xdr()
        decoded = decode_batch(encoded)
        self.assertEqual(len(decoded), 1)
        self.assertEqual(decoded[0].source.account_id, source.account_id)
        self.assertEqual(decoded[0].destination.account_id, destination.account_id)
        self.assertEqual(decoded[0].amount, transaction.amount)

    def test_decode_multiple_transactions(self):
        # Create and encode multiple transactions
        transactions = [
            Transaction(AccountID("GABCDEF12345678901234567890123456789012345678901234567890123456"),
                        AccountID("GXYZABC12345678901234567890123456789012345678901234567890123456"),
                        100.0),
            Transaction(AccountID("G12345678901234567890123456789012345678901234567890123456789012"),
                        AccountID("G98765432109876543210987654321098765432109876543210987654321098"),
                        200.0)
        ]
        encoded = encode_batch(transactions)
        decoded = decode_batch(encoded)
        self.assertEqual(len(decoded), 2)

if __name__ == '__main__':
    unittest.main()
