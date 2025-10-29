import turtle as trtl
import time
import random

# ----- setup -----

# image file used for each "apple" (here a pear image is used)
apple_image = "pear.gif"

# set up the window/screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)  # make the window full-screen relative to display
wn.bgpic("background.gif")       # background image for the game
wn.addshape(apple_image)         # register custom shape for apple sprites
wn.tracer(False)                 # turn off automatic animation updates for manual control

# game constants and state
NUM_APPLES = 5
apple_list = []                  # list that will hold turtle objects for apples
letters = list("asdfghjkl")      # pool of letters available to assign to apples
current_letters = []             # current letters shown on screen for each apple

# create turtle objects for apples and initialize them (hidden initially)
for _ in range(NUM_APPLES):
    a = trtl.Turtle()
    a.penup()                    # don't draw lines when moving apples
    a.shape(apple_image)         # set sprite image
    a.hideturtle()               # start hidden until positioned
    apple_list.append(a)

# single drawer turtle used for writing letters on the screen (reused)
drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()

# ----- functions -----

def get_random_letter():
    """
    Remove and return a random letter from the letter pool.
    Returns None if no letters remain.
    """
    if not letters:
        return None
    index = random.randint(0, len(letters) - 1)
    return letters.pop(index)

def create_apples():
    """
    Position all apples across the top of the screen, assign each a random letter,
    and draw the corresponding letter next to the apple.
    """
    global current_letters
    current_letters = []            # reset current letters list
    start_x = -200                  # starting x-position for first apple
    spacing = 100                   # spacing between apples
    
    for i in range(NUM_APPLES):
        a = apple_list[i]
        a.goto(start_x + i * spacing, 150)  # place apple at top area
        a.showturtle()                       # make the apple visible
        
        letter = get_random_letter()         # pick a random available letter
        current_letters.append(letter)       # store letter for this apple
        draw_letter(letter, a)               # draw the letter near the apple
        
    wn.update()  # update the screen once after positioning all apples

def draw_letter(letter, apple_turtle):
    """
    Draw a single letter (uppercase) near the given apple_turtle using the shared drawer.
    If letter is None, this will write 'None' so callers should avoid passing None.
    """
    drawer.goto(apple_turtle.xcor() - 18, apple_turtle.ycor() - 40)
    drawer.color("white")
    # draw uppercase letter with large bold Arial font
    drawer.write(letter.upper(), font=("Arial", 55, "bold"))

def apple_fall(active_index):
    """
    Animate the apple at active_index falling to the bottom of the screen.
    Uses accelerating fall (incrementing counter) for a simple gravity effect.
    After falling, reset the apple (reassign letter, reposition).
    """
    active_apple = apple_list[active_index]
    counter = 0
    new_x = active_apple.xcor()
    new_y = active_apple.ycor()
    
    # move the apple down until it reaches y = -170
    while new_y > -170:
        counter += 1
        new_y -= counter
        active_apple.goto(new_x, new_y)
        wn.update()
        time.sleep(0.05)  # small delay to control animation speed
    
    reset_apple(active_index)

def reset_apple(index):
    """
    Hide the apple, assign it a new random letter (if available),
    move it back to the top, redraw all letters, and show the apple if it has a letter.
    """
    global current_letters
    active_apple = apple_list[index]
    active_apple.hideturtle()
    
    # get a new letter from the pool (may be None if pool empty)
    new_letter = get_random_letter()
    current_letters[index] = new_letter  
    
    # move apple back to top y position; keep same x
    new_x = active_apple.xcor()
    new_y = 150
    active_apple.goto(new_x, new_y)
    
    # clear all drawn letters and redraw based on current_letters
    drawer.clear()
  
    for i in range(NUM_APPLES):
        if current_letters[i]:
            draw_letter(current_letters[i], apple_list[i])
    
    # only show the apple again if it has an assigned letter
    if new_letter:
        active_apple.showturtle()
    
    wn.update()

def check_keypress(key):
    """
    Called when a key is pressed. If the pressed key matches one of the current letters,
    find the index of that letter and make the corresponding apple fall.
    """
    if key in current_letters:
        try:
            index = current_letters.index(key)
            apple_fall(index)
        except ValueError:
            # index() raised ValueError if key not found; ignore safely
            pass

def make_key_handler(letter):
    """
    Return a no-argument handler function that will check the given letter when called.
    This is used to register per-letter keypress handlers with the turtle window.
    """
    def handler():
        check_keypress(letter)
    return handler

def set_key_listeners():
    """
    Register keypress handlers for each letter key used in the game.
    Using onkeypress so handlers trigger when the key is pressed.
    """
    for letter in "asdfghjkl":
        wn.onkeypress(make_key_handler(letter), letter)

# ----- start -----

create_apples()
set_key_listeners()
wn.listen()
wn.mainloop()
