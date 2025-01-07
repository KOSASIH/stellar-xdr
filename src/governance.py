from typing import List, Dict, Any
import json
import uuid
from datetime import datetime, timedelta

class Proposal:
    def __init__(self, title: str, description: str, duration: int):
        self.id = str(uuid.uuid4())  # Unique identifier for the proposal
        self.title = title
        self.description = description
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=duration)  # Duration in days
        self.votes: Dict[str, bool] = {}  # Dictionary to track votes (user_id: vote)

    def is_active(self) -> bool:
        """Check if the proposal is still active."""
        return datetime.now() < self.end_time

    def vote(self, user_id: str, support: bool):
        """Cast a vote for the proposal."""
        if user_id in self.votes:
            raise ValueError("User  has already voted on this proposal.")
        if not self.is_active():
            raise ValueError("Voting period has ended.")
        self.votes[user_id] = support

    def get_results(self) -> Dict[str, Any]:
        """Get the results of the proposal."""
        if self.is_active():
            raise ValueError("Proposal is still active. Results are not available yet.")
        total_votes = len(self.votes)
        if total_votes == 0:
            return {"support": 0, "against": 0, "total": 0}

        support_count = sum(1 for vote in self.votes.values() if vote)
        return {
            "support": support_count,
            "against": total_votes - support_count,
            "total": total_votes
        }

class Governance:
    def __init__(self):
        self.proposals: List[Proposal] = []

    def create_proposal(self, title: str, description: str, duration: int) -> Proposal:
        """Create a new governance proposal."""
        proposal = Proposal(title, description, duration)
        self.proposals.append(proposal)
        return proposal

    def get_active_proposals(self) -> List[Proposal]:
        """Get a list of active proposals."""
        return [proposal for proposal in self.proposals if proposal.is_active()]

    def get_proposal_by_id(self, proposal_id: str) -> Proposal:
        """Get a proposal by its ID."""
        for proposal in self.proposals:
            if proposal.id == proposal_id:
                return proposal
        raise ValueError("Proposal not found.")

if __name__ == "__main__":
    governance = Governance()

    # Example usage
    proposal = governance.create_proposal("Increase Supply", "Proposal to increase the supply of Pi Coin.", 7)
    print(f"Created Proposal: {proposal.title} (ID: {proposal.id})")

    # Simulate voting
    try:
        proposal.vote("user1", True)
        proposal.vote("user2", False)
    except ValueError as e:
        print(e)

    # Check results after the voting period
    if not proposal.is_active():
        results = proposal.get_results()
        print(f"Proposal Results: {results}")
