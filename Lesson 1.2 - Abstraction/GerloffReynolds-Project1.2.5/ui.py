import turtle

def initialize_ui(screen, font, current_alberts):
    drawer = turtle.Turtle()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(200, 200)
    drawer.write(f"Score: {current_alberts}", align="center", font=font)
    screen.update()
    return drawer

def draw_upgrades_sidebar(screen, upgrades_list):
    sidebar = turtle.Turtle()
    sidebar.penup()
    sidebar.hideturtle()
    sidebar.speed(0)
    sidebar.goto(250, 250)
    sidebar.pendown()
    sidebar.pensize(3)
    sidebar.setheading(0)
    sidebar.forward(250)
    sidebar.right(90)
    sidebar.forward(400)
    sidebar.right(90)
    sidebar.forward(250)
    sidebar.right(90)
    sidebar.forward(400)
    sidebar.penup()

    # Upgrades Header
    sidebar.goto(260, 230)
    sidebar.write("Upgrades", font=("Arial", 20, "bold"))

    # Draw upgrade boxes
    box_y_start = 200
    box_height = 50
    box_width = 200
    for idx, upgrade in enumerate(upgrades_list):
        y = box_y_start - idx * (box_height + 10)
        draw_upgrade_box(sidebar, 260, y, box_width, box_height, upgrade)

def draw_upgrade_box(t, x, y, w, h, upgrade):
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.penup()
    t.goto(x + 10, y - 30)
    # Show upgrade name and description/cost
    display_text = f"{upgrade['name']}\nCost: {upgrade['cost']}\n{upgrade.get('description', '')}"
    t.write(display_text, font=("Arial", 12, "normal"))
