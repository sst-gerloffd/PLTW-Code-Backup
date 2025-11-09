import turtle

runner = turtle.Turtle()
runner.shape("turtle")
runner.color("red")
runner.pendown()  

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

def enable_controls(screen):
    screen.onkeypress(up, "Up")
    screen.onkeypress(down, "Down")
    screen.onkeypress(left, "Left")
    screen.onkeypress(right, "Right")
    screen.listen()
