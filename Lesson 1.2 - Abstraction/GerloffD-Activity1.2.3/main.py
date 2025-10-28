import turtle as trtl
import time

#-----setup-----
apple_image = "pear.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.tracer(False)  # Turn off automatic updates for manual control

apple = trtl.Turtle()

#-----functions-----
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()

def apple_fall(active_apple): 
    counter = 0
    new_x = active_apple.xcor()
    new_y = active_apple.ycor()

    while new_y > -170:  # stop lower so you can see it
        counter += 1  # simulate acceleration
        new_y -= counter

        active_apple.penup()
        active_apple.goto(new_x, new_y)

        wn.update()      # refresh the screen each move
        time.sleep(0.05) # small delay so motion is visible

#-----function calls-----
draw_apple(apple)
apple_fall(apple)

wn.mainloop()
