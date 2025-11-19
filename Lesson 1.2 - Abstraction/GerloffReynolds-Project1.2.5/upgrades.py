class Upgrade:

    def __init__(self, name, base_cost, cps_increase=0, click_increase=0):
        self.name = name
        self.level = 0
        self.base_cost = base_cost
        self.cps_increase = cps_increase
        self.click_increase = click_increase

    def cost(self):
        return int(self.base_cost * (1.15 ** self.level))

    def purchase(self, current_alberts):
        price = self.cost()
        if current_alberts >= price:
            current_alberts -= price
            self.level += 1
            return True, current_alberts
        return False, current_alberts


mini_albert = Upgrade(name="Mini Albert", base_cost=50, cps_increase=0.10)
click_upgrade = Upgrade(name="Click Power", base_cost=100, click_increase=1)

def total_cps():
    return mini_albert.level * mini_albert.cps_increase


def total_click_power(base_clicks):
    return base_clicks + click_upgrade.level * click_upgrade.click_increase
