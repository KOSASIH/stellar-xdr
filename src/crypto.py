import nacl.signing
import nacl.encoding

def sign_transaction(transaction_data: bytes, private_key: str) -> bytes:
    signing_key = nacl.signing.SigningKey(private_key.encode('utf-8'))
    signed = signing_key.sign(transaction_data)
    return signed.signature

def verify_signature(transaction_data: bytes, signature: bytes, public_key: str) -> bool:
    verify_key = nacl.signing.VerifyKey(public_key.encode('utf-8'))
    try:
        verify_key.verify(transaction_data, signature)
        return True
    except nacl.exceptions.BadSignatureError:
        return False
