import json
import os
from datetime import datetime
from typing import List, Dict, Any

class Notification:
    def __init__(self, user_id: str, message: str, timestamp: str):
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        """Convert the notification to a dictionary for easy serialization."""
        return {
            "user_id": self.user_id,
            "message": self.message,
            "timestamp": self.timestamp
        }

class NotificationManager:
    def __init__(self):
        self.notifications_file = "notifications.json"  # File to store notifications
        self.notifications: List[Notification] = self.load_notifications()

    def load_notifications(self) -> List[Notification]:
        """Load notifications from a file."""
        if os.path.exists(self.notifications_file):
            with open(self.notifications_file, "r") as file:
                notifications_data = json.load(file)
                return [Notification(**notif) for notif in notifications_data]
        return []

    def send_notification(self, user_id: str, message: str):
        """Send a notification to a user."""
        timestamp = datetime.now().isoformat()
        notification = Notification(user_id, message, timestamp)
        self.notifications.append(notification)
        self.save_notifications()
        print(f"Notification sent to {user_id}: {message}")

    def save_notifications(self):
        """Save the notifications to a file."""
        with open(self.notifications_file, "w") as file:
            json.dump([notif.to_dict() for notif in self.notifications], file, indent=4)

    def get_notifications_for_user(self, user_id: str) -> List[Notification]:
        """Retrieve notifications for a specific user."""
        return [notif for notif in self.notifications if notif.user_id == user_id]

    def generate_report(self) -> str:
        """Generate a summary report of all notifications."""
        report = {
            "total_notifications": len(self.notifications),
            "notifications": [notif.to_dict() for notif in self.notifications]
        }
        report_file = f"notification_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Notification report generated: {report_file}")
        return report_file

if __name__ == "__main__":
    notification_manager = NotificationManager()

    # Example usage
    notification_manager.send_notification("user1", "Your transaction has been processed.")
    notification_manager.send_notification("user2", "A new governance proposal has been created.")

    # Retrieve notifications for a user
    user_notifications = notification_manager.get_notifications_for_user("user1")
    print(f"Notifications for user1: {[notif.to_dict() for notif in user_notifications]}")

    # Generate a report
    notification_manager.generate_report()
