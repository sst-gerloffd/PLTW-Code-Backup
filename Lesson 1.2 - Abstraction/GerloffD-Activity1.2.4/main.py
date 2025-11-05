import turtle

# --- Configuration / constants ---
num_walls = 25           # total number of wall segments to draw
path_width = 20          # base step used to increase each wall length
wall_color = "black"     # color used for the drawn walls
door_offset = 10         # distance from the segment start to the start of the door
door_width = path_width  # width of the door (here equal to the base path width)

# --- Turtle setup ---
t = turtle.Turtle()
t.pensize(2) # thickness of the lines
t.speed(0)   # fastest drawing speed
t.pencolor(wall_color)

# --- Loop state ---
loop_counter = 0          # how many wall segments we've drawn so far
step_amount = path_width  # current full length of the next wall segment

''' 
Draw `num_walls` segments. Each iteration draws one straight piece of wall
with a door-gap somewhere near its start, then turns right 90 degrees to
prepare for the next segment. The segment length grows by `path_width` each
time so the walls spiral outward.
'''

while loop_counter < num_walls:
        # Draw the first part of the wall up to the door
        t.forward(door_offset)

        # Create the door: lift pen (so nothing is drawn), move forward the door width, then put the pen down to continue drawing the wall after the gap.
        t.penup()
        t.forward(door_width)
        t.pendown()

        # Draw the remainder of the current wall segment. The remainder length is the total step amount minus the part before the door and the door width.
        t.forward(step_amount - door_offset - door_width)

        # Turn to build the next side of the spiral and increase the length for the next segment so the drawing expands outward.
        t.right(90)
        step_amount += path_width
        loop_counter += 1

turtle.done()
