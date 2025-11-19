import turtle
import clicker
import ui
import upgrades
import math
import random

screen = turtle.Screen()
click_value = 1
balance = 0
total_earned = 0
score_font = ("roboto", 18, "bold")
albert_image = "albert.gif"
screen.addshape(albert_image)
albert = turtle.Turtle()
albert.shape(albert_image)

upgrades_list = [
    {"name": "Onramps Effect", "cost": "50", "description": "- 50% Alberts"},
    {"name": "Mini Albert", "cost": str(upgrades.mini_albert.cost()), "description": "+0.1 CPS"},
    {"name": "Click Power", "cost": str(upgrades.click_upgrade.cost()), "description": "+1 per click"},
]

score_drawer = ui.initialize_ui(screen, score_font, balance)
upgrade_boxes = ui.draw_upgrades_sidebar(screen, upgrades_list)
mini_alberts = []


def format_score(n):
    if abs(n - round(n)) < 0.001:
        return str(int(round(n)))
    return f"{n:.1f}"


def update_score_display():
    score_drawer.clear()
    score_drawer.write(f"Score: {format_score(balance)}", align="center", font=score_font)


def on_albert_click(x, y):
    global balance, total_earned
    power = upgrades.total_click_power(click_value)
    balance, total_earned = clicker.click(x, y, power, balance, total_earned)
    update_score_display()


def try_buy_upgrade(box_index):
    global balance, upgrade_boxes
    row = upgrades_list[box_index]
    name = row['name']

    if name == 'Mini Albert':
        bought, new_balance = upgrades.mini_albert.purchase(balance)
        if bought:
            balance = new_balance
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.shape('circle')
            t.shapesize(0.6)
            t.color('gold')
            t.showturtle()
            mini_alberts.append({
                't': t,
                'angle': random.uniform(0, 2 * math.pi),
                'radius': 60,
                'speed': 0.12
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
        return

    if name == 'Mini Albert':
        row['cost'] = str(upgrades.mini_albert.cost())
    elif name == 'Click Power':
        row['cost'] = str(upgrades.click_upgrade.cost())

    upgrade_boxes = ui.draw_upgrades_sidebar(screen, upgrades_list)
    update_score_display()


def passive_tick():
    global balance, total_earned
    cps = upgrades.total_cps()
    balance += cps
    total_earned += cps
    update_score_display()
    screen.ontimer(passive_tick, 1000)


def on_screen_click(x, y):
    for i, b in enumerate(upgrade_boxes):
        left = b['x']
        right = b['x'] + b['w']
        top = b['y']
        bottom = b['y'] - b['h']
        if left <= x <= right and bottom <= y <= top:
            try_buy_upgrade(i)
            break


def animate_minis():
    for m in mini_alberts:
        m['angle'] += m['speed']
        cx = albert.xcor()
        cy = albert.ycor()
        x = cx + math.cos(m['angle']) * m['radius']
        y = cy + math.sin(m['angle']) * m['radius']
        m['t'].goto(x, y)
    screen.ontimer(animate_minis, 50)


passive_tick()
screen.onclick(on_screen_click)
albert.onclick(on_albert_click)
animate_minis()
turtle.done()
