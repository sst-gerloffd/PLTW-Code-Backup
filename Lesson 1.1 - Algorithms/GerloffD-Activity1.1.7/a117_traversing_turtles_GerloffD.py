import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

#  Defines Starting Variables
startx = 0 
starty = 0
direction = 90

# Moves the turtles up and and foward
for t in my_turtles:   
    new_color = turtle_colors.pop() # Change turtle color
    t.pencolor(new_color)
    t.fillcolor(new_color)

    t.setheading(direction)
    t.goto(startx, starty)  # Start at the last turtle's end point
    direction = t.heading()

    t.pendown()
    t.right(45)     
    t.forward(50)

    # Update the startx and starty for the next turtle
    startx = t.xcor()
    starty = t.ycor()
    
    direction -= 45

wn = trtl.Screen()
wn.mainloop()