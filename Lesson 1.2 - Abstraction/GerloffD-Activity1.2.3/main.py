import turtle as trtl
import time

#-----setup-----

apple_image = "pear.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.tracer(False)  # Turn off automatic updates for manual control

drawer = trtl.Turtle()
apple = trtl.Turtle()

drawer.penup()
drawer.hideturtle()

apple.goto(0,0)

#-----functions-----

def draw_an_A():
  apple_fall(apple)
  
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()

def apple_fall(active_apple): 
    counter = 0
    new_x = active_apple.xcor()
    new_y = active_apple.ycor()
    
    if active_apple.ycor() != -170:
      while new_y > -170:  # stop lower so you can see it
        counter += 1  # simulate acceleration
        new_y -= counter

        active_apple.penup()
        active_apple.goto(new_x, new_y)

        wn.update()      # refresh the screen each move
        time.sleep(0.05) # small delay so motion is visible
      else:
        drawer.clear()
        active_apple.hideturtle()        
        wn.update()
    

#-----function calls-----

draw_apple(apple)

drawer.goto(-18,-40)

drawer.color("white")
drawer.write("A", font=("Arial", 55, "bold")) 

wn.onkeypress(draw_an_A, "a")
wn.listen()

wn.mainloop()
