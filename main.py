import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 500
dX = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Movement mechanics
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dX = -0.5
            if event.key == pygame.K_RIGHT:
                dX = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dX = 0
    
    # Background
    screen.fill((0,0,0))
    
    # Player
    playerX += dX

    # Stop at boundaries
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    player(playerX, playerY)

    pygame.display.update()