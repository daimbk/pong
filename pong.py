import pygame

# pygame setup
pygame.init()
fps = 60
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
running = True
clock = pygame.time.Clock()
dt = 0 # delta time in seconds since last frame

# colors
TEAL = (0, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up the players
player_color = TEAL
player_width = 10
player_height = 100
player_speed = 2

player1_x = player_width + 50
player1_y = height // 2
player2_x = (width - player_width) - 50
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

    # move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= 300 * dt * player_speed
    if keys[pygame.K_s]:
        player1_y += 300 * dt * player_speed

    if keys[pygame.K_UP]:
        player2_y -= 300 * dt * player_speed
    if keys[pygame.K_DOWN]:
        player2_y += 300 * dt * player_speed

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(fps) / 1000

pygame.quit()
