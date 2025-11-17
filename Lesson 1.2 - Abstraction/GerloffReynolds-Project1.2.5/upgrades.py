# === upgrades.py === #
class Upgrade:
    def __init__(self, name, base_cost, cps_increase=0, click_increase=0):
        self.name = name
        self.level = 0
        self.base_cost = base_cost
        self.cps_increase = cps_increase      # clicks per second
        self.click_increase = click_increase  # clicks per click

    def cost(self):
        # Cost increases exponentially with level
        return int(self.base_cost * (1.15 ** self.level))

    def purchase(self, current_alberts):
        if current_alberts >= self.cost():
            current_alberts -= self.cost()
            self.level += 1
            return True, current_alberts
        return False, current_alberts

# === Upgrade Instances === #
mini_albert = Upgrade(
    name="Mini Albert",
    base_cost=50,          # Starting cost
    cps_increase=0.10      # Each mini Albert adds 0.1 CPS
)

click_upgrade = Upgrade(
    name="Click Power",
    base_cost=100,
    click_increase=1       # Each level increases clicks per click by 1
)

# === Helper Functions === #
def total_cps():
    return mini_albert.level * mini_albert.cps_increase # Calculates total clicks per second from all upgrades."""

def total_click_power(base_clicks):
    return base_clicks + click_upgrade.level * click_upgrade.click_increase # Calculates current clicks per click including upgrades.
