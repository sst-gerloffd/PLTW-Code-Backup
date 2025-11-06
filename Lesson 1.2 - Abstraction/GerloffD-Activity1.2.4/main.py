import turtle

num_walls = 25
path_width = 20
wall_color = "black"
door_offset = 10
door_width = path_width
barrier_offset = 40
barrier_length = path_width

t = turtle.Turtle()
t.pensize(2)
t.speed(0)
t.pencolor(wall_color)

loop_counter = 0
step_amount = path_width

while loop_counter < num_walls:
    if loop_counter < 5:
        t.penup()
        t.forward(step_amount)
        t.right(90)
        step_amount += path_width
        loop_counter += 1
        continue

    t.forward(door_offset)
    t.penup()
    t.forward(door_width)
    t.pendown()

    t.forward(barrier_offset)
    t.left(90)
    t.forward(40)
    t.backward(40)
    t.right(90)

    t.forward(step_amount - door_offset - door_width - barrier_offset)
    t.right(90)
    step_amount += path_width
    loop_counter += 1

turtle.done()
