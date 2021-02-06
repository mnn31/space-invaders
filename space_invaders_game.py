#############################################
## SPACE INVADERS GAME
## By: Manan Gupta
## Date: December 2020
## Made in Python Programming Level-2 Course
## asset gold scholar programme
###############################################

import pygame
import math, random

def load_image(img):
    return pygame.image.load(img)

def get_num_enemies():
    return random.randint(5, 9)

###############################################
################ MAIN #########################

# Initializing module          
pygame.init()

score = 0

# Creating a screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Changing title of screen
pygame.display.set_caption('SPACE INVADERS GAME')

# Changing icon of window
screen_icon = load_image('icon.png')
pygame.display.set_icon(screen_icon)

# Loading background image
background_img = load_image('bgspace.jpg')

# Adding player to screen
player_img = load_image('battleship.png')
player_x = 400
player_y = 500
xchange = 0

# Adding bullet to screen
bullet_img = load_image('blt2.png')
bullet_x = 400
bullet_y = 550
bullet_ychange = 6
bullet_state = 'ready'

# Adding enemy to screen
enemy_img = []       # Empty list to load enemy images
enemy_x = []         # Empty list to add x coordinate for every image
enemy_y = []         # Empty list to add x coordinate for every image
enemy_xchange = []   # Empty list to add change of x coordinate for every image
enemy_ychange = []   # Empty list to add change of x coordinate for every image
num_enemies = get_num_enemies()

for i in range(num_enemies):
    enemy_img.append(load_image('alien.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_xchange.append(7)
    enemy_ychange.append(20)
################################################################################

def bullet():
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (bullet_x, bullet_y))

def player():
    screen.blit(player_img, (player_x, player_y))

def enemy():
    screen.blit(enemy_img[i], (enemy_x[i], enemy_y[i]))

def show_text(txt, val, x, y):
    font = pygame.font.SysFont('courier', 30)
    text = font.render(f'{txt}: {val}', True, (255, 255, 255))
    screen.blit(text, (x, y))
    

def show_score():
    show_text("Score", score, 10, 10)

def show_num_enemies():
    show_text("Enemies", num_enemies, 500, 10)
 
def game_over():
    font = pygame.font.SysFont('courier', 34)
    text = font.render('Game Over! The alien has captured you.', True, (255,255,143))
    screen.blit(text, (0, 300))

#################################################################################
        
running = True

# Game forever loop
while running:
    screen.fill((0,0,143))
    # Adding background image
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard Bindings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -5
                
            if event.key == pygame.K_RIGHT:
                xchange = 5
                
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = pygame.mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bullet_x = player_x + 16
                    bullet()

                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0
                
#################################################################
    # Player movement
    player_x += xchange

    # Preventing player from leaving screen
    if player_x <= 0:
        player_x = 0

    if player_x >= 736:
        player_x = 736  
##############################################################
        
    # Bullet movement
    if bullet_state == 'fire':
        bullet()
        bullet_y -= bullet_ychange
        
    # Preventing bullet from leaving screen
    if bullet_y <= 0:
        bullet_y = 500
        bullet_state = 'ready'
        
##############################################################

    # Enemy movement
    for i in range(num_enemies):
#############################################################
        # Game over
        if enemy_y[i] >= player_y:
            game_over()
            for t in range(num_enemies):
                enemy_y[t] = 1000
#############################################################
            
        enemy_x[i] += enemy_xchange[i]
        if enemy_x[i] >= 736:
            enemy_xchange[i] = -1
            enemy_y[i] += enemy_ychange[i]
            
        elif enemy_x[i] <= 0:
            enemy_xchange[i] = 1
            enemy_y[i] += enemy_ychange[i]

        # Finding distance between enemy and bullet
        distance = math.sqrt((math.pow(bullet_x - enemy_x[i], 2)) + 
                              (math.pow(bullet_y - enemy_y[i], 2)))
        if distance <= 25:
            hit_sound = pygame.mixer.Sound('explosion.wav')
            hit_sound.play()
            bullet_y = 550
            bullet_state = 'ready'
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)
            score += 10
                             

        # Calling enemy() function to display enemy on screen
        enemy()
############################################################
        
    # Calling player() function to display player on screen
    player()

    # Showing score
    show_score()
    show_num_enemies()

    # Updating screen
    pygame.display.update()

# Closing pygame window
pygame.quit()
