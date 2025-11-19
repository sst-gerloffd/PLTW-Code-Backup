"""
Simple, commented main game file.

This version keeps the same behavior as before but uses friendlier names
and lots of comments so a student can explain what's happening.
"""

# === imports ===
import turtle
import clicker
import ui
import upgrades
import math
import random

# === setup / game state ===
# screen is the Turtle window where everything is drawn
screen = turtle.Screen()

# How many Alberts you get when you click Albert
click_value = 1

# Current number of Alberts the player has (the "score" / currency)
balance = 0

# Total Alberts ever earned (for tracking, not used everywhere)
total_earned = 0

# Font used to show the score
score_font = ("roboto", 18, "bold")

# Main Albert image (keeps the original project behavior)
albert_image = "albert.gif"
screen.addshape(albert_image)
albert = turtle.Turtle()
albert.shape(albert_image)

# === upgrades data used for the sidebar display ===
# We store a small list for the UI. The actual logic (levels, cost)
# lives inside upgrades.py (Upgrade instances).
upgrades_list = [
    {"name": "Onramps Effect", "cost": "50", "description": "- 50% Alberts"},
    {"name": "Mini Albert", "cost": str(upgrades.mini_albert.cost()), "description": "+0.1 CPS"},
    {"name": "Click Power", "cost": str(upgrades.click_upgrade.cost()), "description": "+1 per click"},
]

# Create the UI elements
score_drawer = ui.initialize_ui(screen, score_font, balance)
# draw the sidebar and get the clickable box locations (so we can detect clicks)
upgrade_boxes = ui.draw_upgrades_sidebar(screen, upgrades_list)

# A simple list of mini-Albert objects. Each mini is a dict with
# a small turtle and some values to animate it.
mini_alberts = []


# === helper functions ===
def format_score(n):
    """Return a human-friendly string for the score.

    We keep numbers simple (no long decimals) so it's easier to explain.
    """
    # If the number is basically an integer, show it without decimals
    if abs(n - round(n)) < 0.001:
        return str(int(round(n)))
    # Otherwise show one decimal place for small fractional CPS effects
    return f"{n:.1f}"


def update_score_display():
    """Clear and redraw the score text at the top of the screen."""
    score_drawer.clear()
    score_drawer.write(f"Score: {format_score(balance)}", align="center", font=score_font)


def on_albert_click(x, y):
    """When the big Albert is clicked, add Alberts to the balance.

    x and y are provided by Turtle but not needed here.
    """
    global balance, total_earned
    # current click power takes into account click upgrades
    power = upgrades.total_click_power(click_value)
    balance, total_earned = clicker.click(x, y, power, balance, total_earned)
    update_score_display()


def try_buy_upgrade(box_index):
    """Try to buy the upgrade represented by the sidebar box index.

    If the player has enough Alberts we buy the upgrade using the
    Upgrade.purchase method in `upgrades.py` which returns (success, new_balance).
    If the purchase is for a Mini Albert we also spawn a small turtle that
    orbits the main Albert (a simple visual reward).
    """
    global balance, upgrade_boxes
    row = upgrades_list[box_index]
    name = row['name']

    if name == 'Mini Albert':
        bought, new_balance = upgrades.mini_albert.purchase(balance)
        if bought:
            balance = new_balance
            # spawn a small gold circle to be a mini-Albert
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.shape('circle')
            t.shapesize(0.6)
            t.color('gold')
            t.showturtle()
            # add a simple animation state for the mini
            mini_alberts.append({
                't': t,
                'angle': random.uniform(0, 2 * math.pi),
                'radius': 60,    # fixed radius so behavior is predictable
                'speed': 0.12    # fixed speed for simple explanation
            })
        else:
            return

    elif name == 'Click Power':
        bought, new_balance = upgrades.click_upgrade.purchase(balance)
        if bought:
            balance = new_balance
        else:
            return

    else:
        # If other upgrades are added later, handle them here
        return

    # After a successful purchase update the cost text in the UI
    # The cost comes from the Upgrade instance so it increases as level grows
    if name == 'Mini Albert':
        row['cost'] = str(upgrades.mini_albert.cost())
    elif name == 'Click Power':
        row['cost'] = str(upgrades.click_upgrade.cost())

    # redraw sidebar and update the boxes we use for click detection
    upgrade_boxes = ui.draw_upgrades_sidebar(screen, upgrades_list)
    update_score_display()


def passive_tick():
    """Called every second to add passive Alberts from upgrades (CPS).

    We call this with ontimer so students can understand it's a repeating timer.
    """
    global balance, total_earned
    cps = upgrades.total_cps()
    balance += cps
    total_earned += cps
    update_score_display()
    screen.ontimer(passive_tick, 1000)


def on_screen_click(x, y):
    """Detect if a click happened inside any upgrade box; if so, try to buy it.

    The UI module gives us box rectangles (top-left x,y coordinates plus w,h).
    """
    for i, b in enumerate(upgrade_boxes):
        left = b['x']
        right = b['x'] + b['w']
        top = b['y']
        bottom = b['y'] - b['h']
        if left <= x <= right and bottom <= y <= top:
            try_buy_upgrade(i)
            break


def animate_minis():
    """Move each mini-Albert in a small circle around the main Albert.

    This is simple math (cos, sin) and helps give a visual reward when
    the player buys the mini upgrade.
    """
    for m in mini_alberts:
        m['angle'] += m['speed']
        cx = albert.xcor()
        cy = albert.ycor()
        x = cx + math.cos(m['angle']) * m['radius']
        y = cy + math.sin(m['angle']) * m['radius']
        m['t'].goto(x, y)
    # call again after 50ms to keep animating
    screen.ontimer(animate_minis, 50)


# === start the game loops and event handlers ===
passive_tick()               # start the 1-second passive income timer
screen.onclick(on_screen_click)  # catches clicks anywhere (used for buying upgrades)
albert.onclick(on_albert_click)  # clicking the big Albert gives Alberts
animate_minis()              # start mini animation loop

turtle.done()  # keep the window open and listen for events
