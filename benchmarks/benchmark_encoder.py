import timeit
from src.encoder import encode_batch
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

# Benchmarking function
def benchmark_encode(num_transactions):
    transactions = create_sample_transactions(num_transactions)
    encode_batch(transactions)

if __name__ == "__main__":
    num_transactions = 1000  # Adjust the number of transactions for benchmarking
    execution_time = timeit.timeit(lambda: benchmark_encode(num_transactions), number=10)
    print(f"Encoding {num_transactions} transactions took {execution_time:.4f} seconds.")
