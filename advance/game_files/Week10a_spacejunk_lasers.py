# SEV Advanced - Week 10 Lasers

import pgzrun
from random import *

WIDTH = 1000
HEIGHT = 600

# keep track of score
score = 0

SCOREBOX_HEIGHT = 60  # height of the box displaying the score
X_SPEED = 5  # speed of moving objects
BACKGROUND_IMG = "space_game_background"
PLAYER_IMG = "player_ship"
JUNK_IMG = "space_junk"
LASER_IMG = "laser_red"

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

# INITIALIZE LASERS
lasers = []

# game loop             
def update():
    updatePlayer()
    updateJunk()
    updateLasers()# need to update our lasers first so our program know to reposition debris or satellite
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
    for laser in lasers: # make sure to use a for loop to draw lasers
        laser.draw()

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

    # check for firing lasers
    if keyboard.space == 1:
        laser = Actor(LASER_IMG)
        laser.pos = (player.centerx, player.centery)
        fireLasers(laser) # fireLasers is a function to adjust timing of lasers (students will use template)

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
        
def updateLasers():
    global score, lasers
    for laser in lasers:  # for each laser in the lasers list 
        laser.x += -5  # lasers moving towards the left, so negative x direction
        # remove laser if moves off screen
        if laser.right < 0:
            lasers.remove(laser)
        # check for collisions
        if debris.colliderect(laser) == 1:
            lasers.remove(laser)
            debris.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - debris.height))
            score += 5
        if satellite.colliderect(laser) == 1:
            lasers.remove(laser)
            satellite.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height))
            score += -5
            
###################################
# activating lasers (template code)____________________________________________________________________________________________
player.laserActive = 1  # add laserActive status to the player

def makeLaserActive():  # when called, this function will make lasers active again
    global player
    player.laserActive = 1

def fireLasers(laser):
    if player.laserActive == 1:  # active status is used to prevent continuous shoot when holding space key
        player.laserActive = 0
        clock.schedule(makeLaserActive, 0.2)  # schedule an event (function, time afterwhich event will occur)
        sounds.laserfire02.play()  # play sound effect
        lasers.append(laser)  # add laser to lasers list
        
pgzrun.go()


