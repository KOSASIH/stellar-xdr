# ai_pi_value_setter/utils.py

import logging
import json
import hashlib
import base64
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Utils:
    """
    Utils provides ultra high-tech utility functions for the Pi Network ecosystem,
    including hashing, encoding, timestamp formatting, and JSON serialization helpers.
    """

    @staticmethod
    def sha256_hash(data: bytes) -> str:
        """
        Computes SHA-256 hash of the given data.

        Args:
            data (bytes): Data to hash.

        Returns:
            str: Hexadecimal SHA-256 hash string.
        """
        hash_digest = hashlib.sha256(data).hexdigest()
        logger.debug(f"SHA-256 hash computed: {hash_digest}")
        return hash_digest

    @staticmethod
    def base64_encode(data: bytes) -> str:
        """
        Encodes bytes into Base64 string.

        Args:
            data (bytes): Data to encode.

        Returns:
            str: Base64 encoded string.
        """
        encoded = base64.b64encode(data).decode('utf-8')
        logger.debug(f"Base64 encoded data: {encoded}")
        return encoded

    @staticmethod
    def base64_decode(data_str: str) -> bytes:
        """
        Decodes Base64 string into bytes.

        Args:
            data_str (str): Base64 encoded string.

        Returns:
            bytes: Decoded bytes.
        """
        decoded = base64.b64decode(data_str.encode('utf-8'))
        logger.debug(f"Base64 decoded data: {decoded}")
        return decoded

    @staticmethod
    def json_serialize(obj, *, indent=2) -> str:
        """
        Serializes a Python object to a JSON string with indentation.

        Args:
            obj: Python object to serialize.
            indent (int): Number of spaces for indentation.

        Returns:
            str: JSON formatted string.
        """
        try:
            json_str = json.dumps(obj, indent=indent, sort_keys=True)
            logger.debug(f"JSON serialized object: {json_str}")
            return json_str
        except (TypeError, ValueError) as e:
            logger.error(f"JSON serialization error: {e}")
            raise

    @staticmethod
    def json_deserialize(json_str: str):
        """
        Deserializes a JSON string into a Python object.

        Args:
            json_str (str): JSON formatted string.

        Returns:
            object: Python object.
        """
        try:
            obj = json.loads(json_str)
            logger.debug(f"JSON deserialized object: {obj}")
            return obj
        except (json.JSONDecodeError, TypeError) as e:
            logger.error(f"JSON deserialization error: {e}")
            raise

    @staticmethod
    def current_utc_timestamp() -> str:
        """
        Returns the current UTC timestamp in ISO 8601 format.

        Returns:
            str: Current UTC timestamp string.
        """
        timestamp = datetime.utcnow().isoformat() + 'Z'
        logger.debug(f"Current UTC timestamp: {timestamp}")
        return timestamp

    @staticmethod
    def verify_integrity(data: bytes, expected_hash_hex: str) -> bool:
        """
        Verifies the integrity of data by comparing its SHA-256 hash to an expected hash.

        Args:
            data (bytes): Data to verify.
            expected_hash_hex (str): Expected SHA-256 hash in hex.

        Returns:
            bool: True if hashes match, False otherwise.
        """
        actual_hash = Utils.sha256_hash(data)
        is_valid = actual_hash == expected_hash_hex.lower()
        logger.debug(f"Integrity verification: expected={expected_hash_hex.lower()}, actual={actual_hash}, valid={is_valid}")
        return is_valid

# Internal test example
if __name__ == "__main__":
    test_data = b"Ultra high-tech Pi Network data"
    hash_hex = Utils.sha256_hash(test_data)
    encoded = Utils.base64_encode(test_data)
    decoded = Utils.base64_decode(encoded)
    json_str = Utils.json_serialize({"data": "test", "value": 314159})
    obj = Utils.json_deserialize(json_str)
    timestamp = Utils.current_utc_timestamp()
    integrity = Utils.verify_integrity(test_data, hash_hex)

    print(f"SHA-256 Hash: {hash_hex}")
    print(f"Base64 Encoded: {encoded}")
    print(f"Base64 Decoded: {decoded}")
    print(f"JSON Serialized: {json_str}")
    print(f"JSON Deserialized: {obj}")
    print(f"Current UTC Timestamp: {timestamp}")
    print(f"Integrity Verified: {integrity}")
