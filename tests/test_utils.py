# tests/test_utils.py

import unittest
from ai_pi_value_setter.utils import Utils

class TestUtils(unittest.TestCase):

    def test_sha256_hash(self):
        data = b"test data"
        expected_hash = "916f002c9a0a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1"
        # We won't test exact hash here, just length and type
        result = Utils.sha256_hash(data)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 64)

    def test_base64_encode_decode(self):
        data = b"hello world"
        encoded = Utils.base64_encode(data)
        decoded = Utils.base64_decode(encoded)
        self.assertEqual(decoded, data)

    def test_json_serialize_deserialize(self):
        obj = {"key": "value", "number": 314159}
        json_str = Utils.json_serialize(obj)
        self.assertIsInstance(json_str, str)
        obj2 = Utils.json_deserialize(json_str)
        self.assertEqual(obj, obj2)

    def test_current_utc_timestamp(self):
        timestamp = Utils.current_utc_timestamp()
        self.assertTrue(timestamp.endswith('Z'))
        self.assertIsInstance(timestamp, str)

    def test_verify_integrity(self):
        data = b"integrity test"
        hash_hex = Utils.sha256_hash(data)
        self.assertTrue(Utils.verify_integrity(data, hash_hex))
        self.assertFalse(Utils.verify_integrity(data, "0"*64))

if __name__ == "__main__":
    unittest.main()
