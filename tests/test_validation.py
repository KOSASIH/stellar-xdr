import unittest
from src.validation import validate_account_id

class TestValidation(unittest.TestCase):
    def test_valid_account_id(self):
        self.assertTrue(validate_account_id("GABCDEF12345678901234567890123456789012345678901234567890123456"))

    def test_invalid_account_id_length(self):
        self.assertFalse(validate_account_id("GABCDEF123456789012345678901234567890123456789012345678901234567"))

    def test_invalid_account_id_format(self):
        self.assertFalse(validate_account_id("INVALID_ACCOUNT_ID"))

if __name__ == '__main__':
    unittest.main()
