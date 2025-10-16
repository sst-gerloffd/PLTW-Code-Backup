# a121_catch_a_turtle.py
#-----import statements-----

import turtle
import random as rand                                                           

#-----game configuration----

spot = turtle.Turtle()
spot_color = "pink"
spot_shape = "circle" # Possible shapes are: “arrow,” “turtle,” “circle,” “square,” “triangle,” and “classic.” 
spot_shapesize = 1.5
score = 0 # Global variable that scores the current user score

#-----initialize turtle-----

spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_shapesize)

#-----game functions--------

def turtle_click(x, y):
    change_position()

def change_position():
    new_x = rand.randint(-400, 400) # Generates new x and y coordinates
    new_y = rand.randint(-300, 300)
    
    spot.penup()
    spot.goto(new_x,new_y) # Moves to new position.
    spot.pendown()


def update_global_score():
  global score # This will update the global score.
  score += 1
  print(score)
    
#-----events----------------

spot.onclick(turtle_click)

wn = turtle.Screen()
wn.mainloop()
