import turtle

t = turtle.Turtle()
t.speed(0)

loop_counter = 0
target = 20  
step_amount = 10  

while loop_counter < target:
    t.forward(step_amount)
    t.right(90)
    
    step_amount += 10
    loop_counter += 1

turtle.done()
