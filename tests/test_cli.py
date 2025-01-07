import unittest
import subprocess

class TestCLI(unittest.TestCase):
    def test_cli_encode(self):
        result = subprocess.run(['python', 'src/cli.py', 'encode', 'GABCDEF12345678901234567890123456789012345678901234567890123456', 
                                 'GXYZABC12345678901234567890123456789012345678901234567890123456', '100.0'], 
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Encoded XDR:", result.stdout)

    def test_cli_decode(self):
        # Assuming we have a valid XDR hex string for testing
        xdr_hex = "some_valid_xdr_hex_string"
        result = subprocess.run(['python', 'src/cli.py', 'decode', xdr_hex], 
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Decoded Transactions", result.stdout)

if __name__ == '__main__':
    unittest.main()
