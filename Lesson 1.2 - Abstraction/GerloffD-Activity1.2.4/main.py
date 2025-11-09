import turtle, random
import runner  # import the runner module

# --- setup ---
wn = turtle.Screen()
t = turtle.Turtle()
t.pensize(2)
t.speed(0)
t.pencolor("black")

num_walls = 25
path_width = 20
step = path_width

# --- draw the maze ---
for i in range(num_walls):
    if i < 5:
        t.penup()
        t.forward(step)
        t.right(90)
        step += path_width
        continue

    door = random.randint(10, step - 30)
    barrier = random.randint(10, step - 30)
    while abs(door - barrier) < 25:
        barrier = random.randint(10, step - 30)

    if door < barrier:
        first, second = "door", "barrier"
        first_pos, second_pos = door, barrier
    else:
        first, second = "barrier", "door"
        first_pos, second_pos = barrier, door

    t.forward(first_pos)
    if first == "door":
        t.penup(); t.forward(path_width); t.pendown()
    else:
        t.left(90); t.forward(40); t.backward(40); t.right(90)

    t.forward(second_pos - first_pos - path_width)
    if second == "door":
        t.penup(); t.forward(path_width); t.pendown()
    else:
        t.left(90); t.forward(40); t.backward(40); t.right(90)

    t.forward(step - second_pos - path_width)
    t.right(90)
    step += path_width

# --- start game ---
t.hideturtle()
runner.runner.goto(0, 0)
runner.enable_controls(wn)
wn.mainloop()
