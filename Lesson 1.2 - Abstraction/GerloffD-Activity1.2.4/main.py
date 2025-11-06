import turtle, random

# --- setup ---

t = turtle.Turtle()
t.pensize(4)
t.speed(0)
t.pencolor("black")

num_walls = 30      # number of walls in the spiral
path_width = 20     # space between each wall
step = path_width   # how far each wall extends
barrier_length = path_width + 20


# --- maze setup ---

for i in range(num_walls):
    # draw first few walls with no doors or barriers
    if i < 5:
        t.penup()
        t.forward(step)
        t.right(90)
        step += path_width
        continue

    # pick random spots for door and barrier
    door = random.randint(10, step - 30)
    barrier = random.randint(10, step - 30)

    # make sure they aren’t too close together
    while abs(door - barrier) < 25:
        barrier = random.randint(10, step - 30)

    # figure out which comes first
    if door < barrier:
        first, second = "door", "barrier"
        first_pos, second_pos = door, barrier
    else:
        first, second = "barrier", "door"
        first_pos, second_pos = barrier, door

    # move to first item
    t.forward(first_pos)
    if first == "door":
        t.penup(); t.forward(path_width); t.pendown()       # draw door (gap)
    else:
        t.left(90); t.forward(barrier_length); t.backward(barrier_length); t.right(90)  # draw barrier

    # move to second item
    t.forward(second_pos - first_pos - path_width)
    if second == "door":
        t.penup(); t.forward(path_width); t.pendown()
    else:
        t.left(90); t.forward(barrier_length); t.backward(barrier_length); t.right(90)

    # finish rest of the wall and turn
    t.forward(step - second_pos - path_width)
    t.right(90)
    step += path_width


turtle.done()
