import json
import os
from datetime import datetime
from typing import List, Dict, Any
from src.transaction_history import TransactionHistory

class Analytics:
    def __init__(self):
        self.transaction_history = TransactionHistory()  # Load transaction history
        self.analytics_file = "analytics_report.json"  # File to store analytics reports

    def calculate_total_transactions(self) -> int:
        """Calculate the total number of transactions."""
        return len(self.transaction_history.get_all_transactions())

    def calculate_total_volume(self) -> float:
        """Calculate the total volume of transactions."""
        total_volume = sum(tx.amount for tx in self.transaction_history.get_all_transactions())
        return total_volume

    def calculate_user_engagement(self) -> Dict[str, int]:
        """Calculate user engagement metrics."""
        user_engagement = {}
        for tx in self.transaction_history.get_all_transactions():
            user_engagement[tx.sender] = user_engagement.get(tx.sender, 0) + 1
            user_engagement[tx.receiver] = user_engagement.get(tx.receiver, 0) + 1
        return user_engagement

    def generate_report(self) -> str:
        """Generate a summary report of the analytics."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_transactions": self.calculate_total_transactions(),
            "total_volume": self.calculate_total_volume(),
            "user_engagement": self.calculate_user_engagement()
        }
        report_file = f"analytics_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Analytics report generated: {report_file}")
        return report_file

if __name__ == "__main__":
    analytics = Analytics()
    analytics.generate_report()
