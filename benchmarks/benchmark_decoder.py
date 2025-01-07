import timeit
from src.decoder import decode_batch
from src.xdr_types import Transaction, AccountID

# Create sample data for benchmarking
def create_sample_transactions(num_transactions):
    transactions = []
    for i in range(num_transactions):
        source = AccountID(f"GABCDEF12345678901234567890123456789012345678901234567890123456{i}")
        destination = AccountID(f"GXYZABC12345678901234567890123456789012345678901234567890123456{i}")
        transaction = Transaction(source, destination, float(i + 1) * 100.0)
        transactions.append(transaction)
    return transactions

# Function to encode transactions to XDR for decoding
def encode_transactions(num_transactions):
    transactions = create_sample_transactions(num_transactions)
    return encode_batch(transactions)

# Benchmarking function
def benchmark_decode(num_transactions):
    xdr_data = encode_transactions(num_transactions)
    decode_batch(xdr_data)

if __name__ == "__main__":
    num_transactions = 1000  # Adjust the number of transactions for benchmarking
    execution_time = timeit.timeit(lambda: benchmark_decode(num_transactions), number=10)
    print(f"Decoding {num_transactions} transactions took {execution_time:.4f} seconds.")
