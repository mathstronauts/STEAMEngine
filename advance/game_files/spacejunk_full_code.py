# SEV Advanced - Space Junk Full Code 

import pgzrun
from random import *

WIDTH = 1000
HEIGHT = 600
SCOREBOX_HEIGHT = 50  # change to height of scoreboard

# keep track of score
score = 0

# sprite speeds
junk_speed = 5
sat_speed = 3
debris_speed = 5

# image files
BACKGROUND_IMG = "space_game_background"
PLAYER_IMG = "player_ship"
JUNK_IMG = "space_junk"
SATELLITE_IMG = "satellite_adv"
DEBRIS_IMG = "space_debris2"
LASER_IMG = "laser_red"

# initialize sprites
# sprite_name = Actor("file_name", rect_pos = (x, y))
player = Actor(PLAYER_IMG)
player.midright = (WIDTH - 15, HEIGHT/2)

# initialize junk sprites
junks = []  # list to keep track of junks
for i in range(5):
    junk = Actor(JUNK_IMG)  # create a junk sprite
    x_pos = randint(-500, -50)
    y_pos = randint(SCOREBOX_HEIGHT, HEIGHT - junk.height)
    junk.topright = (x_pos, y_pos)  # rect_position = (x, y)
    junks.append(junk)
    
# initialize satellite
satellite = Actor(SATELLITE_IMG)  # create sprite
x_sat = randint(-500, -50)
y_sat = randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height)
satellite.topright = (x_sat, y_sat)  # rect_position

# initialize debris
debris = Actor(DEBRIS_IMG)
x_deb = randint(-500, -50)
y_deb = randint(SCOREBOX_HEIGHT, HEIGHT - debris.height)
debris.topright = (x_deb, y_deb)

# INITIALIZE LASERS
lasers = []

# play background music
sounds.spacelife.play(-1)  # sounds.file_name.play(loop_num), if want to loop indefinitely until stop(), enter -1

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
    if player.top < SCOREBOX_HEIGHT:
        player.top = SCOREBOX_HEIGHT
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

    # check for firing lasers
    if keyboard.space == 1:
        laser = Actor(LASER_IMG)
        laser.pos = (player.centerx, player.centery)
        fireLasers(laser) # fireLasers is a function to adjust timing of lasers (students will use template)

def updateJunk():
    global score
    for junk in junks:  # add for loop
        junk.x += junk_speed  # same as junk.x = junk.x + 3
    
        collision = player.colliderect(junk)  # declare collision variable

        if junk.left > WIDTH or collision == 1:  # make junk reappear if move off screen
            x_pos = randint(-500, -50) # start off screen
            y_pos = randint(SCOREBOX_HEIGHT, HEIGHT - junk.height)
            junk.topright = (x_pos, y_pos)

        if collision == 1: # if collisions occurs 
            score += 1  # this is the same score = score + 1
            sounds.collect_pep.play()  # sounds.file_name.play()

def updateDebris():
    global score
    debris.x += debris_speed  # or just put 3
    collision = player.colliderect(debris)

    if debris.left > WIDTH or collision == 1:
        x_deb = randint(-500, -50)
        y_deb = randint(SCOREBOX_HEIGHT, HEIGHT - debris.height)
        debris.topright = (x_deb, y_deb)

    if collision == 1:
        score += -10

def updateSatellite():
    global score
    satellite.x += sat_speed  # or just put 3
    collision = player.colliderect(satellite)

    if satellite.left > WIDTH or collision == 1:
        x_sat = randint(-500, -50)
        y_sat = randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height)
        satellite.topright = (x_sat, y_sat)

    if collision == 1:
        score += -10   
        
def updateLasers():
    global score, lasers
    for laser in lasers:  # for each laser in the lasers list 
        laser.x += -5  # lasers moving towards the left, so negative x direction
        collision_debris = debris.colliderect(laser)
        collision_satellite = satellite.colliderect(laser)
        # remove laser if moves off screen
        if laser.right < 0 or collision_debris == 1 or collision_satellite == 1:
            lasers.remove(laser)
        # check for collisions
        if collision_debris == 1:
            debris.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - debris.height))
            score += 5
            sounds.explosion.play()
        if collision_satellite == 1:
            satellite.topright = (randint(-500, -50), randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height))
            score += -5
            sounds.explosion.play()
            
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



