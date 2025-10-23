# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# return names in the leaderboard file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this
  names = []
  
  for line in leaderboard_file:
    leader_name = ""
    index = 0

    # read characters for the name until comma or end of line
    while index < len(line) and line[index] != "," and line[index] != "\n":
      leader_name = leader_name + line[index]
      index = index + 1

    if leader_name != "":
      names.append(leader_name)

  print(names)
  leaderboard_file.close()
  return names
  
# return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")
  scores = []
  
  for line in leaderboard_file:
    leader_score = ""
    index = 0

    # skip characters until after the comma
    while index < len(line) and line[index] != ",":
      index += 1
      
    # move past the comma if present
    if index < len(line) and line[index] == ",":
      index += 1
      
    # read characters for the score until end of line or newline
    while index < len(line) and line[index] != "\n":
      leader_score += line[index]
      index += 1

    if leader_score != "":
      scores.append(int(leader_score))   # convert to int here

  print(scores)
  leaderboard_file.close()
  return scores

def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):

  index = 0
  # loop through all the scores in the existing leaderboard list
  for score in leader_scores:
    # check if this is the position to insert new score at (higher scores first)
    if player_score >= int(score):
      break
    else:
      index = index + 1

  # insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)

  # keep both lists at 5 elements only (top 5 players)
  while len(leader_names) > 5:
    leader_names.pop()
    leader_scores.pop()

  # store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start

  # loop through all the leaderboard elements and write them to the file
  for i in range(len(leader_names)):
    leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")

  leaderboard_file.close()
   
  
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()

  # loop through the lists and use the same index to display the corresponding name and score
  for index in range(len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()

  # display message about player making/not making leaderboard
  if high_scorer:
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # display medal message
  if player_score >= gold_score:
    turtle_object.write("You earned a gold medal!", font=font_setup)
  elif player_score >= silver_score:
    turtle_object.write("You earned a silver medal!", font=font_setup)
  elif player_score >= bronze_score:
    turtle_object.write("You earned a bronze medal!", font=font_setup)
