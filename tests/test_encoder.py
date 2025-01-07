import unittest
from src.encoder import encode_batch
from src.xdr_types import Transaction, AccountID

class TestEncoder(unittest.TestCase):
    def test_encode_single_transaction(self):
        source = AccountID("GABCDEF12345678901234567890123456789012345678901234567890123456")
        destination = AccountID("GXYZABC12345678901234567890123456789012345678901234567890123456")
        transaction = Transaction(source, destination, 100.0)
        encoded = encode_batch([transaction])
        self.assertEqual(len(encoded), 120)  # Example length check

    def test_encode_multiple_transactions(self):
        transactions = [
            Transaction(AccountID("GABCDEF12345678901234567890123456789012345678901234567890123456"),
                        AccountID("GXYZABC12345678901234567890123456789012345678901234567890123456"),
                        100.0),
            Transaction(AccountID("G12345678901234567890123456789012345678901234567890123456789012"),
                        AccountID("G98765432109876543210987654321098765432109876543210987654321098"),
                        200.0)
        ]
        encoded = encode_batch(transactions)
        self.assertEqual(len(encoded), 240)  # Example length check

if __name__ == '__main__':
    unittest.main()
