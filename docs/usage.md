# Usage of Stellar XDR

This section provides examples of how to use the Stellar XDR library for serialization and validation of data.

## Serialization Example

To serialize data into XDR format, you can use the `XDRSerializer` class. Here’s an example:

```python
1 from src.xdr_serializer import XDRSerializer
2 
3 data = {
4     "source": "GABCDEF12345678901234567890123456789012345678901234567890123456",
5     "destination": "GXYZABC12345678901234567890123456789012345678901234567890123456",
6     "amount": 100.0
7 }
8 
9 serialized_data = XDRSerializer.serialize(data)
10 print(f"Serialized XDR: {serialized_data.hex()}")
```

## Validation Example
To validate data structures, you can use the XDRValidator class. Here’s an example:

```python
1 from src.xdr_validator import XDRValidator
2 
3 data = {
4     "source": "GABCDEF12345678901234567890123456789012345678901234567890123456",
5     "destination": "GXYZABC12345678901234567890123456789012345678901234567890123456",
6     "amount": 100.0
7 }
8 
9 is_valid = XDRValidator.validate(data)
10 if is_valid:
11     print("Data is valid.")
12 else:
13     print("Data is invalid.")
```

## Conclusion
By implementing these advanced features, the stellar-xdr project can become a more robust and user-friendly library for developers working with the Stellar network. Each of these components enhances the functionality and usability of the library, making it easier to integrate and work with XDR data structures.
