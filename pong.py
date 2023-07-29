import pygame

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
running = True

# colors
TEAL = (0, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up the players
player_color = TEAL
player_width = 10
player_height = 100
player_speed = 2

player1_x = (width - player_width) - 50
player1_y = height // 2
player2_x = player_width + 50
player2_y = height // 2

# game loop
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # draw players
    pygame.draw.rect(screen, TEAL, (player1_x, player1_y, player_width, player_height))
    pygame.draw.rect(screen, TEAL, (player2_x, player2_y, player_width, player_height))

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
