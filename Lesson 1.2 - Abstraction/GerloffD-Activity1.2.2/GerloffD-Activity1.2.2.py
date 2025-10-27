#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_fall(apple): 
    counter = 0
    new_x = 10
    new_y = apple.ycor()
    
    while new_y > -10: # Example stop at y = -100
        counter += 1 # Increase counter (acceleration)
        
        # Calculate new position
        new_y = new_y - counter
        
        # Update the position
        apple.penup()
        apple.goto(new_x, new_y)

#-----function calls-----
draw_apple(apple)
apple_fall(apple)

wn.mainloop()
