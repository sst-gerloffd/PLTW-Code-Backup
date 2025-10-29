import turtle as trtl
import time
import random

# ----- setup -----

apple_image = "pear.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image)
wn.tracer(False)

drawer = trtl.Turtle()
apple = trtl.Turtle()

drawer.penup()
drawer.hideturtle()
apple.penup()

apple.goto(0, 0)

# ----- letter setup -----

letters = list("asdfghjkl")

# ----- functions -----

def get_random_letter():
    """Get a random letter from the list using pop and randint."""
    if not letters:
        return None  # No letters left
    index = random.randint(0, len(letters) - 1)
    return letters.pop(index)

def draw_letter(letter):
    """Write the given letter on screen."""
    drawer.clear()
    drawer.goto(-18, -40)
    drawer.color("white")
    drawer.write(letter.upper(), font=("Arial", 55, "bold"))

def apple_fall(active_apple): 
    counter = 0
    new_x = active_apple.xcor()
    new_y = active_apple.ycor()

    if active_apple.ycor() != -170:
        while new_y > -170:
            counter += 1
            new_y -= counter
            active_apple.goto(new_x, new_y)
            wn.update()
            time.sleep(0.05)
        else:
            drawer.clear()
            active_apple.hideturtle()
            wn.update()

def drop_apple():
    """Trigger the fall animation and redraw a new random letter."""
    apple_fall(apple)
    draw_new_apple()

def draw_new_apple():
    """Draw a new apple with a random letter."""
    global current_letter
    apple.showturtle()
    apple.shape(apple_image)
    current_letter = get_random_letter()
    if current_letter:
        draw_letter(current_letter)
        wn.onkeypress(drop_apple, current_letter)  # Bind to that letter
    wn.update()

# ----- start -----

draw_new_apple()
wn.listen()
wn.mainloop()
