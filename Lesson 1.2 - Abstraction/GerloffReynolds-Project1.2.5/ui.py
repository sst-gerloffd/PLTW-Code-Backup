import turtle

_sidebar_drawer = None


def initialize_ui(screen, font, current_alberts):
    drawer = turtle.Turtle()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(0, 230)
    drawer.write(f"Score: {current_alberts}", align="center", font=font)
    screen.update()
    return drawer


def draw_upgrades_sidebar(screen, upgrades_list):
    global _sidebar_drawer
    if _sidebar_drawer is not None:
        try:
            _sidebar_drawer.clear()
            _sidebar_drawer.hideturtle()
        except Exception:
            pass

    drawer = turtle.Turtle()
    _sidebar_drawer = drawer
    drawer.penup()
    drawer.hideturtle()
    drawer.speed(0)

    # Draw the border for the sidebar
    drawer.goto(200, 250)
    drawer.pendown()
    drawer.pensize(3)
    for _ in range(2):
        drawer.forward(250)
        drawer.right(90)
        drawer.forward(480)
        drawer.right(90)
    drawer.penup()

    drawer.goto(210, 220)
    drawer.write("Upgrades", font=("Arial", 20, "bold"))

    box_y_start = 180
    box_height = 70
    box_width = 230

    boxes = []
    for i, upgrade in enumerate(upgrades_list):
        y = box_y_start - i * (box_height + 10)
        draw_upgrade_box(drawer, 210, y, box_width, box_height, upgrade)
        boxes.append({
            'x': 210,
            'y': y,
            'w': box_width,
            'h': box_height,
            'name': upgrade['name']
        })

    return boxes


def draw_upgrade_box(t, x, y, w, h, upgrade):
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.penup()

    t.goto(x + 5, y - 20)
    display_text = f"{upgrade['name']}  |  Cost: {upgrade['cost']}"
    t.write(display_text, font=("Arial", 12, "bold"))

    t.goto(x + 5, y - 40)
    if "description" in upgrade:
        t.write(upgrade["description"], font=("Arial", 10, "normal"))

