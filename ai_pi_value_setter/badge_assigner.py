# ai_pi_value_setter/badge_assigner.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class BadgeAssigner:
    """
    BadgeAssigner automatically assigns a special badge 🌟 to pure Pi Coins.
    Pure Pi Coins are those mined, transacted P2P, or contributed within the ecosystem.
    This badge is attached as metadata to the Pi Coin object.
    """

    STAR_BADGE = "🌟"

    def __init__(self):
        logger.info("BadgeAssigner initialized.")

    def assign_badge(self, pi_coin):
        """
        Assigns the star badge 🌟 to the Pi Coin if it is pure.

        Args:
            pi_coin (object): Pi Coin object expected to have 'is_pure' (bool) and 'badge' (str or None) attributes.

        Returns:
            pi_coin (object): The Pi Coin object with badge assigned if pure.
        """
        if not hasattr(pi_coin, 'is_pure'):
            logger.error("Pi Coin object missing 'is_pure' attribute")
            raise AttributeError("Pi Coin object must have 'is_pure' attribute")

        if not hasattr(pi_coin, 'badge'):
            # Initialize badge attribute if missing
            setattr(pi_coin, 'badge', None)

        if pi_coin.is_pure:
            pi_coin.badge = self.STAR_BADGE
            logger.info(f"Assigned badge {self.STAR_BADGE} to pure Pi Coin.")
        else:
            pi_coin.badge = None
            logger.info("Pi Coin is not pure; badge removed if existed.")

        return pi_coin

# Internal test example
if __name__ == "__main__":
    class DummyPiCoin:
        def __init__(self, is_pure):
            self.is_pure = is_pure
            self.badge = None

        def __repr__(self):
            return f"<DummyPiCoin is_pure={self.is_pure} badge={self.badge}>"

    assigner = BadgeAssigner()

    pure_coin = DummyPiCoin(is_pure=True)
    impure_coin = DummyPiCoin(is_pure=False)

    print("Before badge assignment:")
    print(pure_coin)
    print(impure_coin)

    pure_coin = assigner.assign_badge(pure_coin)
    impure_coin = assigner.assign_badge(impure_coin)

    print("\nAfter badge assignment:")
    print(pure_coin)
    print(impure_coin)
