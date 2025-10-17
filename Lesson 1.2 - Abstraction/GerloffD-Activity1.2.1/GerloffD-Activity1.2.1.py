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

score_writer = turtle.Turtle() # Score display turtle and font setup
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-350, 260)  # Move score_writer to top-left area of screen; adjust as needed
score_writer.write(f"Score: {score}") # Initialize displayed score

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
    update_score()


def update_score():
    global score  # use the global score variable
    score += 1
    
    # erase previous score and write updated score
    score_writer.clear()
    score_writer.write(f"Score: {score}")
    
#-----events----------------

spot.onclick(turtle_click)

wn = turtle.Screen()
wn.mainloop()
