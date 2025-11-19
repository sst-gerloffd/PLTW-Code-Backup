import turtle

# Keep a module-level drawer so we can clear the sidebar when updating it
_sidebar_drawer = None


def initialize_ui(screen, font, current_alberts):
    """Create and return a small turtle that writes the score at the top.

    The returned turtle (`drawer`) is used by main.py to update the score.
    """
    drawer = turtle.Turtle()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(0, 230)
    drawer.write(f"Score: {current_alberts}", align="center", font=font)
    screen.update()
    return drawer


def draw_upgrades_sidebar(screen, upgrades_list):
    """Draw the upgrades area on the right side and return clickable boxes.

    Returns a list of dicts. Each dict has: x, y, w, h, name. The x,y is the
    top-left corner of the box. main.py uses these boxes to tell if the
    player clicked on an upgrade.
    """
    global _sidebar_drawer
    # If we have drawn a sidebar before, clear it so we don't draw on top
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
        drawer.forward(250)   # width
        drawer.right(90)
        drawer.forward(480)   # height
        drawer.right(90)
    drawer.penup()

    # Title
    drawer.goto(210, 220)
    drawer.write("Upgrades", font=("Arial", 20, "bold"))

    # Box layout
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
    """Draw a single upgrade box and show its name, cost and a short note.

    t: turtle used to draw
    x,y: top-left of box
    w,h: width & height
    upgrade: dict with keys 'name', 'cost', and optionally 'description'
    """
    # Draw the rectangle
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.penup()

    # Write the name and cost
    t.goto(x + 5, y - 20)
    display_text = f"{upgrade['name']}  |  Cost: {upgrade['cost']}"
    t.write(display_text, font=("Arial", 12, "bold"))

    # Optional small description below
    t.goto(x + 5, y - 40)
    if "description" in upgrade:
        t.write(upgrade["description"], font=("Arial", 10, "normal"))
