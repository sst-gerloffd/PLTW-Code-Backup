import turtle

def initialize_ui(screen, font, current_alberts):
    drawer = turtle.Turtle()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(0, 230)
    drawer.write(f"Score: {current_alberts}", align="center", font=font)
    screen.update()
    return drawer


def draw_upgrades_sidebar(screen, upgrades_list):
    sidebar = turtle.Turtle()
    sidebar.penup()
    sidebar.hideturtle()
    sidebar.speed(0)

    # Sidebar border
    sidebar.goto(200, 250)
    sidebar.pendown()
    sidebar.pensize(3)
    for _ in range(2):
        sidebar.forward(250)   # width
        sidebar.right(90)
        sidebar.forward(480)   # height
        sidebar.right(90)
    sidebar.penup()

    # Header
    sidebar.goto(210, 220)
    sidebar.write("Upgrades", font=("Arial", 20, "bold"))

    # Draw boxes
    box_y_start = 180
    box_height = 70
    box_width = 230

    for i, upgrade in enumerate(upgrades_list):
        y = box_y_start - i * (box_height + 10)
        draw_upgrade_box(sidebar, 210, y, box_width, box_height, upgrade)


def draw_upgrade_box(t, x, y, w, h, upgrade):
    # Box outline
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.penup()

    # Text inside the box
    t.goto(x + 5, y - 20)
    display_text = f"{upgrade['name']}  |  Cost: {upgrade['cost']}"
    t.write(display_text, font=("Arial", 12, "bold"))

    t.goto(x + 5, y - 40)
    if "description" in upgrade:
        t.write(upgrade["description"], font=("Arial", 10, "normal"))
