# === imports === #
import turtle
import clicker
import ui

# === setup === #
screen = turtle.Screen()
alberts_per_click = 1
total_alberts = 0
current_alberts = 0
current_score_font = ("roboto", 18, "bold")

albert_image = "Emre.gif"
screen = turtle.Screen()

screen.addshape(albert_image)

albert = turtle.Turtle()
albert.shape(albert_image)

# Initialize UI and store the drawer object
current_score_drawer = ui.initialize_ui(screen, current_score_font, current_alberts)

# === Run Game === #
def handle_click(x, y):
    global current_alberts, total_alberts, alberts_per_click

    current_alberts, total_alberts = clicker.click(x, y, alberts_per_click, current_alberts, total_alberts)

    current_score_drawer.clear()
    current_score_drawer.write(f"Score: {current_alberts}", align="center", font=current_score_font)



albert.onclick(handle_click)
turtle.done()