import argparse
from .encoder import encode_batch
from .decoder import decode_batch ```python
from .xdr_types import Transaction, AccountID

def main():
    parser = argparse.ArgumentParser(description='XDR Encoder/Decoder for Stellar')
    parser.add_argument('--encode', help='Encode transactions to XDR', nargs='+', metavar='TRANSACTION')
    parser.add_argument('--decode', help='Decode XDR to transactions', type=str)

    args = parser.parse_args()

    if args.encode:
        transactions = []
        for tx_data in args.encode:
            # Assuming tx_data is formatted as "source,destination,amount"
            source_id, destination_id, amount = tx_data.split(',')
            transaction = Transaction(AccountID(source_id), AccountID(destination_id), float(amount))
            transactions.append(transaction)
        xdr_data = encode_batch(transactions)
        print(f'Encoded XDR: {xdr_data.hex()}')

    if args.decode:
        xdr_bytes = bytes.fromhex(args.decode)
        transactions = decode_batch(xdr_bytes)
        for tx in transactions:
            print(f'Decoded Transaction: {tx.source.account_id} -> {tx.destination.account_id}, Amount: {tx.amount}')

if __name__ == '__main__':
    main()
