import turtle

def initialize_ui(screen, font, current_alberts):
    drawer = turtle.Turtle()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(200, 200)
    drawer.write(f"Score: {current_alberts}", align="center", font=font)
    screen.update()
    return drawer
