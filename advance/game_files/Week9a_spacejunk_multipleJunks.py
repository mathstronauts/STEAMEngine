# SEV Advanced - Week 2 Collisions
# Students will learn to detect collisions between the junk and player sprites and count score

import pgzrun
from random import *

WIDTH = 1000
HEIGHT = 600

# keep track of score
score = 0

SCOREBOX_HEIGHT = 60
JUNK_X_SPEED = 5
BACKGROUND_IMG = "space_game_background"
PLAYER_IMG = "player_ship"
JUNK_IMG = "space_junk"

player = Actor(PLAYER_IMG, midright = (WIDTH - 15, HEIGHT/2))

# INITIALIZE JUNKS
junks = []
for i in range(5):
    junk = Actor(JUNK_IMG)
    junk.topleft = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - junk.height))
    junks.append(junk)
    
# game loop             
def update():
    updatePlayer()
    updateJunk()
    
def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMG, (0,0))
    player.draw()
    for junk in junks:
        junk.draw()

    # draw some text on the screen
    show_score = "Score: " + str(score)
    screen.draw.text(show_score, topleft=(750, 15), fontsize=35, color="white")


# make separate functions for each of our sprites
def updatePlayer():
    # check for user input
    if keyboard.up == 1:
        player.y += -5  # moving up is in negative y direction
    elif keyboard.down == 1:
        player.y += 5  # moving down is in the postive y direction

    # prevent player from moving off screen
    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

def updateJunk():
    global score
    for junk in junks:
        junk.x += JUNK_X_SPEED   # move junk across screen

        collision = player.colliderect(junk) # colliderect() tests if two rectangles overlap
        if junk.left > WIDTH or collision == 1:
            junk.topleft = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - junk.height))

        # collisions between player and junk
        if collision:
            score += 1  # update the score

pgzrun.go()


