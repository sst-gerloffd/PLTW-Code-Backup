import turtle

# create screen and runner turtle
wn = turtle.Screen()

runner = turtle.Turtle()
runner.shape("turtle")
runner.color("red")
runner.penup()

# --- movement handlers for arrow keys ---

def up():
    runner.setheading(90)
    runner.forward(10)

def down():
    runner.setheading(270)
    runner.forward(10)

def left():
    runner.setheading(180)
    runner.forward(10)

def right():
    runner.setheading(0)
    runner.forward(10)

# bind keypress events to the handlers

wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

# start listening for events
wn.listen()

# keep the window open and processing events
wn.mainloop()
