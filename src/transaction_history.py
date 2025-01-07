import json
import os
from datetime import datetime
from typing import List, Dict, Any

class Transaction:
    def __init__(self, tx_id: str, sender: str, receiver: str, amount: float, timestamp: str):
        self.tx_id = tx_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        """Convert the transaction to a dictionary for easy serialization."""
        return {
            "tx_id": self.tx_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

class TransactionHistory:
    def __init__(self):
        self.history_file = "transaction_history.json"  # File to store transaction history
        self.transactions: List[Transaction] = self.load_history()

    def load_history(self) -> List[Transaction]:
        """Load transaction history from a file."""
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                history_data = json.load(file)
                return [Transaction(**tx) for tx in history_data]
        return []

    def log_transaction(self, sender: str, receiver: str, amount: float):
        """Log a new transaction."""
        tx_id = str(len(self.transactions) + 1)  # Simple ID generation
        timestamp = datetime.now().isoformat()
        transaction = Transaction(tx_id, sender, receiver, amount, timestamp)
        self.transactions.append(transaction)
        self.save_history()
        print(f"Transaction logged: {transaction.to_dict()}")

    def save_history(self):
        """Save the transaction history to a file."""
        with open(self.history_file, "w") as file:
            json.dump([tx.to_dict() for tx in self.transactions], file, indent=4)

    def get_transaction_by_id(self, tx_id: str) -> Transaction:
        """Retrieve a transaction by its ID."""
        for transaction in self.transactions:
            if transaction.tx_id == tx_id:
                return transaction
        raise ValueError("Transaction not found.")

    def get_all_transactions(self) -> List[Transaction]:
        """Get all transactions."""
        return self.transactions

    def generate_report(self) -> str:
        """Generate a summary report of all transactions."""
        report = {
            "total_transactions": len(self.transactions),
            "transactions": [tx.to_dict() for tx in self.transactions]
        }
        report_file = f"transaction_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Transaction report generated: {report_file}")
        return report_file

if __name__ == "__main__":
    transaction_history = TransactionHistory()

    # Example usage
    transaction_history.log_transaction("user1", "user2", 100.0)
    transaction_history.log_transaction("user3", "user4", 50.0)

    # Retrieve a transaction
    try:
        tx = transaction_history.get_transaction_by_id("1")
        print(f"Retrieved Transaction: {tx.to_dict()}")
    except ValueError as e:
        print(e)

    # Generate a report
    transaction_history.generate_report()
