# a116_buggy_image.py
import turtle as trtl
'''
instead of a descriptive name of the turtle such as painter,
a less useful variable name x is used

'''

painter = trtl.Turtle() # x

# Draw Circle
painter.pensize(40)
painter.circle(20)

# Define Legs Parameters
legs = 8 # w
length = 70 # y
degree = 360/legs - 20
painter.pensize(5)
leg_counter = 0 # n

# Draw Legs
while (leg_counter < legs):
  # Draw Section
  painter.goto(0,20)
  
  if leg_counter > 3:
    painter.setheading(degree*leg_counter + 45)
    painter.forward(length)
  else:
    painter.setheading(degree*leg_counter - 45)
    painter.forward(length)

  print("z*n=", degree*leg_counter)
  
  # Counter Section
  leg_counter = leg_counter + 1

# Define Eyes Parameters
painter.pencolor("red")
painter.pensize(10)
eye_counter = 0 # n
x = 15

# Draw Eyes
while eye_counter < 2:
  painter.penup()
  painter.goto(x,0)
  painter.pendown()
  painter.circle(5)
  eye_counter = eye_counter + 1
  x = x - 30

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()