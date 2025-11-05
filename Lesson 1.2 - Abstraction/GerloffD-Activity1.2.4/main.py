import turtle

num_walls = 25
path_width = 20
wall_color = "black"
door_offset = 10
door_width = path_width

t = turtle.Turtle()
t.pensize(2)
t.speed(0)
t.pencolor(wall_color)

loop_counter = 0
step_amount = path_width

while loop_counter < num_walls:
    t.forward(door_offset)

    t.penup()
    t.forward(door_width)
    t.pendown()

    t.forward(step_amount - door_offset - door_width)

    t.right(90)
    step_amount += path_width
    loop_counter += 1

turtle.done()
