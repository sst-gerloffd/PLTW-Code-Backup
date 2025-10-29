import turtle as trtl
import time
import random

# ----- setup -----

apple_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image)
wn.tracer(False)

drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()

# ----- apple setup -----

NUM_APPLES = 5
apple_list = []
letters = list("asdfghjkl")
current_letters = []  # letters for each apple

# ----- functions -----

def get_random_letter():
    """Return a random letter and remove it from letters list."""
    if not letters:
        return None
    index = random.randint(0, len(letters) - 1)
    return letters.pop(index)

def create_apples():
    """Create NUM_APPLES apples and assign letters."""
    global apple_list, current_letters
    apple_list = []
    current_letters = []
    start_x = -200
    spacing = 100
    for i in range(NUM_APPLES):
        a = trtl.Turtle()
        a.penup()
        a.shape(apple_image)
        a.goto(start_x + i * spacing, 150)
        a.showturtle()
        letter = get_random_letter()
        current_letters.append(letter)
        apple_list.append(a)
        draw_letter(letter, a)
    wn.update()

def draw_letter(letter, apple_turtle):
    """Draw a letter above a given apple."""
    drawer.goto(apple_turtle.xcor() - 18, apple_turtle.ycor() - 40)
    drawer.color("white")
    drawer.write(letter.upper(), font=("Arial", 55, "bold"))

def apple_fall(active_index):
    """Animate a specific apple falling down the screen."""
    active_apple = apple_list[active_index]
    counter = 0
    new_x = active_apple.xcor()
    new_y = active_apple.ycor()
    
    while new_y > -170:
        counter += 1
        new_y -= counter
        active_apple.goto(new_x, new_y)
        wn.update()
        time.sleep(0.05)
    
    # Reset the apple to top with new letter
    reset_apple(active_index)

def reset_apple(index):
    """Reset an apple to the top with a new random letter."""
    global current_letters
    active_apple = apple_list[index]
    active_apple.hideturtle()
    
    # Get new random letter
    new_letter = get_random_letter()
    if new_letter is None:
        return  # No letters left
    current_letters[index] = new_letter
    
    # Reset apple position
    new_x = active_apple.xcor()
    new_y = 150
    active_apple.goto(new_x, new_y)
    active_apple.showturtle()
    draw_letter(new_letter, active_apple)
    wn.update()

def check_keypress(key):
    """Check if the pressed key matches any apple's letter."""
    if key in current_letters:
        index = current_letters.index(key)
        apple_fall(index)

def make_key_handler(letter):
    """Return a function that checks a specific key."""
    def handler():
        check_keypress(letter)
    return handler

def set_key_listeners():
    """Attach all key listeners using a helper function."""
    for letter in "asdfghjkl":
        wn.onkeypress(make_key_handler(letter), letter)

# ----- start -----

create_apples()
set_key_listeners()
wn.listen()
wn.mainloop()
