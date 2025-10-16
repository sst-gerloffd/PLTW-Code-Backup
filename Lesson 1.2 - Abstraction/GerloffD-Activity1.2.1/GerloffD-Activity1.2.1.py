# a121_catch_a_turtle.py
#-----import statements-----

import turtle

#-----game configuration----

spot = turtle.Turtle()
spot_color = "pink"
spot_shape = "circle" # Possible shapes are: “arrow,” “turtle,” “circle,” “square,” “triangle,” and “classic.” 
spot_shapesize = 1.5

#-----initialize turtle-----

spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_shapesize)

#-----game functions--------

def turtle_click(x, y):
    print(f"Turtle clicked at: ({x}, {y})")
    
#-----events----------------

spot.onclick(turtle_click)

wn = turtle.Screen()
wn.mainloop()