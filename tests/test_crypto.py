import unittest
from src.crypto import sign_transaction, verify_signature
from nacl.signing import SigningKey, VerifyKey
from nacl.exceptions import BadSignatureError

class TestCrypto(unittest.TestCase):
    def setUp(self):
        # Generate a signing key for testing
        self.signing_key = SigningKey.generate()
        self.verify_key = self.signing_key.verify_key

    def test_sign_transaction(self):
        transaction_data = b"Sample transaction data"
        signature = sign_transaction(transaction_data, self.signing_key.encode(encoder=nacl.encoding.HexEncoder).decode())
        self.assertIsNotNone(signature)

    def test_verify_signature_valid(self):
        transaction_data = b"Sample transaction data"
        signature = sign_transaction(transaction_data, self.signing_key.encode(encoder=nacl.encoding.HexEncoder).decode())
        
        # Verify the signature using the public key
        is_valid = verify_signature(transaction_data, signature, self.verify_key.encode(encoder=nacl.encoding.HexEncoder).decode())
        self.assertTrue(is_valid)

    def test_verify_signature_invalid(self):
        transaction_data = b"Sample transaction data"
        signature = sign_transaction(transaction_data, self.signing_key.encode(encoder=nacl.encoding.HexEncoder).decode())
        
        # Modify the transaction data to create an invalid signature
        modified_data = b"Modified transaction data"
        
        # Verify the signature with modified data
        is_valid = verify_signature(modified_data, signature, self.verify_key.encode(encoder=nacl.encoding.HexEncoder).decode())
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()
