# SEV Beginner - Condensed TEMPLATE

#import libraries
import pgzrun
import random

# set up screen
WIDTH = 800
HEIGHT = 600

background_img = "mars_background"
score = 0 

# initialize characters - Actor("image_file", (x_position, y_position) )
player = Actor("spaceship_beg_up")
player.midbottom = (WIDTH/2, HEIGHT)

#alien = Actor()

# background music

#MAIN GAME LOOP
def update():
    global score 
    # change player ship position and image with keyboard input
    if (keyboard.up == 1) and player.top > 0:
        player.y += -5  
        player.image = "spaceship_beg_up"
    elif (keyboard.down == 1) and player.bottom < HEIGHT:
        player.y += 5  
        player.image = "spaceship_beg_down"
    elif (keyboard.left == 1) and player.left > 0:
        player.x += -5  
        player.image = "spaceship_beg_left"
    elif (keyboard.right == 1) and player.right < WIDTH:
        player.x += 5  
        player.image = "spaceship_beg_right"

    # detect collisions between player and alien
    

def draw():
    #draw background and sprites on screen
    screen.clear()
    screen.blit(background_img, (0, 0))
    player.draw()
    
    #draw score on the screen
    show_score = str(score)
    screen.draw.text(show_score, fontsize=40, topright=(750,21), color='white') 
    
pgzrun.go()
