# === imports === #
import turtle
import clicker
import ui
import upgrades

# === setup === #
screen = turtle.Screen()
alberts_per_click = 1
total_alberts = 0
current_alberts = 0
current_score_font = ("roboto", 18, "bold")
albert_image = "albert.gif"
screen = turtle.Screen()
screen.addshape(albert_image)
albert = turtle.Turtle()
albert.shape(albert_image)

# Initialize Upgrades stuff
upgrades_list = [
    {"name": "Onramps Effect", "cost": "50", "description": "- 50% Alberts"},
    {"name": "Mini Albert", "cost": str(upgrades.mini_albert.cost()), "description": "+0.1 CPS"},
    {"name": "Click Power", "cost": str(upgrades.click_upgrade.cost()), "description": "+1 per click"},
]


# Initialize UI and store the drawer object
current_score_drawer = ui.initialize_ui(screen, current_score_font, current_alberts)
ui.draw_upgrades_sidebar(screen, upgrades_list)

# === Run Game === #
def handle_click(x, y):
    global current_alberts, total_alberts, alberts_per_click

    current_click_power = upgrades.total_click_power(alberts_per_click)
    current_alberts, total_alberts = clicker.click(x, y, current_click_power, current_alberts, total_alberts)

    current_score_drawer.clear()
    current_score_drawer.write(f"Score: {current_alberts}", align="center", font=current_score_font)

def passive_clicks():
    global current_alberts, total_alberts
    cps = upgrades.total_cps()
    current_alberts += cps
    total_alberts += cps
    screen.ontimer(passive_clicks, 1000)  # call every 1000 ms

passive_clicks()
albert.onclick(handle_click)
turtle.done()
