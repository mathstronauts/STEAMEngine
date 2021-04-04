# SEV Beginner - Condensed TEMPLATE

#import libraries
import pgzrun
import random

# set up screen
#WIDTH = 
#HEIGHT = 

background_img = ""
score = 0 

# initialize characters - Actor("image_file", (x_position, y_position) )
#player = Actor()

#alien = Actor()

# background music

#MAIN GAME LOOP
def update():
    global score 
    # change player ship position and image with keyboard input

    # detect collisions between player and alien
  

def draw():
    #draw background and sprites on screen

    #draw score on the screen
    show_score = str(score)
    screen.draw.text(show_score, fontsize=40, topright=(750,21), color='white') 
    
pgzrun.go()
