"""
Simple upgrades module.

This file defines an Upgrade class which tracks the level of an upgrade,
its base cost, and how much it improves clicks-per-second (CPS) or click power.
"""


class Upgrade:
    """Represents one upgrade a player can buy.

    Attributes:
      name: readable name
      level: how many times the player bought it
      base_cost: starting cost (an int)
      cps_increase: how much CPS each level gives (float)
      click_increase: how many extra Alberts per click each level gives (int)
    """

    def __init__(self, name, base_cost, cps_increase=0, click_increase=0):
        self.name = name
        self.level = 0
        self.base_cost = base_cost
        self.cps_increase = cps_increase
        self.click_increase = click_increase

    def cost(self):
        """Return the current cost to buy the next level.

        We increase cost by about 15% per level so each next level is
        more expensive (simple exponential growth).
        """
        return int(self.base_cost * (1.15 ** self.level))

    def purchase(self, current_alberts):
        """Try to buy one level.

        Returns (True, new_balance) if purchase succeeds, otherwise
        (False, old_balance).
        """
        price = self.cost()
        if current_alberts >= price:
            current_alberts -= price
            self.level += 1
            return True, current_alberts
        return False, current_alberts


# === Create the upgrades we want in the game ===
mini_albert = Upgrade(name="Mini Albert", base_cost=50, cps_increase=0.10)
click_upgrade = Upgrade(name="Click Power", base_cost=100, click_increase=1)


def total_cps():
    """Return total clicks-per-second (CPS) coming from upgrades.

    Right now only mini_albert gives CPS: each level adds 0.1 CPS.
    """
    return mini_albert.level * mini_albert.cps_increase


def total_click_power(base_clicks):
    """Return how many Alberts a click gives when considering upgrades.

    base_clicks: the clicks-per-click without upgrades (e.g. 1)
    """
    return base_clicks + click_upgrade.level * click_upgrade.click_increase
