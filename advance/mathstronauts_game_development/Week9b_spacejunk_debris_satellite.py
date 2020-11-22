# SEV Advanced - Week 9 Multiple Sprites - Adding Debris and Satellite

import pgzrun
from random import *

WIDTH = 1000
HEIGHT = 600

# keep track of score
score = 0

SCOREBOX_HEIGHT = 60
X_SPEED = 5
BACKGROUND_IMG = "space_game_background"
PLAYER_IMG = "player_ship"
JUNK_IMG = "space_junk"

player = Actor(PLAYER_IMG)
player.midright = (WIDTH - 15, HEIGHT/2)

# add two more sprites - satellite and debris
debris = Actor("space_debris2")
debris.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - debris.height))

satellite = Actor("satellite_adv")
satellite.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height))

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
    updateDebris()
    updateSatellite()
    
def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMG, (0,0))
    player.draw()
    for junk in junks:
        junk.draw()
    debris.draw()
    satellite.draw()

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
        junk.x += X_SPEED   # move junk across screen

        collision = player.colliderect(junk) # colliderect() tests if two rectangles overlap
        if junk.left > WIDTH or collision == 1:
            junk.topleft = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - junk.height))

        if collision:
            score += 1  # update the score

def updateDebris():
    global score
    debris.x += X_SPEED  # move junk across screen

    collision = player.colliderect(debris) # colliderect() tests if two rectangles overlap
    if debris.left > WIDTH or collision == 1:
        debris.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - debris.height))

    if collision:
        score += -5  # update the score   

def updateSatellite():
    global score
    satellite.x += X_SPEED  # move junk across screen

    collision = player.colliderect(satellite) # colliderect() tests if two rectangles overlap
    if satellite.left > WIDTH or collision == 1:
        satellite.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height))

    if collision:
        score += -5  # update the score   
    
pgzrun.go()


