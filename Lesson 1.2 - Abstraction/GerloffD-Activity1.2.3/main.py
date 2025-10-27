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

def apple_fall():
  counter = 0
  fall_amount = 17
  new_y = apple.xcor()
  
  while counter <= fall_amount:
    new_y -= counter
    
    apple.penup()
    apple.goto(0,new_y) # Moves to new position.
    apple.pendown()
    
    counter += 1

#-----function calls-----
draw_apple(apple)
apple_fall()

wn.mainloop()
