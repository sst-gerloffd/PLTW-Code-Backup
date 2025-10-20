# a121_catch_a_turtle.py
#-----import statements-----

import turtle
import random as rand
import leaderboard as lb

#-----game configuration----

leaderboard_file_name = "leaderboard.txt"
player_name = input ("Please enter your name:")

wn = turtle.Screen()

spot = turtle.Turtle()
spot_color = "pink"
spot_shape = "circle" # Possible shapes are: “arrow,” “turtle,” “circle,” “square,” “triangle,” and “classic.” 
spot_shapesize = 1.5
score = 0 # Global variable that scores the current user score

font_setup = ("Arial", 20, "normal")

score_writer = turtle.Turtle() # Score display turtle and font setup
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-350, 260)  # Move score_writer to top-left area of screen; adjust as needed
score_writer.write(f"Score: {score}", font=font_setup) # Initialize displayed score

#-----countdown configuration-----

timer = 10
timer_up = False

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(200, 260) 
counter.write(timer, font=font_setup)

#-----initialize turtle-----

spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_shapesize)

#-----game functions--------

def turtle_click(x, y):
    global timer_up
    if not timer_up:
        change_position()
    else:
        spot.hideturtle()

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
    
    score_writer.clear() # erase previous score and write updated score
    score_writer.write(f"Score: {score}", font=font_setup)
    
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's up!", font=font_setup)
        timer_up = True
        spot.hideturtle()
        manage_leaderboard() 
    else:
        counter.write(timer, font=font_setup)
        timer -= 1
        wn.ontimer(countdown, 1000) # schedule next call in 1000 ms (1 second)


#-----events----------------

spot.onclick(turtle_click)
wn.ontimer(countdown, 1000)

wn.mainloop()
