import pygame
import player
import ball
from random import choice, randint

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

player1 = player.Player()
player2 = player.Player()
player1.set_x(player_width + 50)
player1.set_y(height // 2)
player2.set_x(width - player_width - 50)
player2.set_y(height // 2)

# set up ball
ball = ball.Ball()
ball_color = WHITE
ball.set_radius(5)
ball.set_x(width // 2)
ball.set_y(height // 2)
ball.set_dx(choice([-2, 2]))
ball.set_dy(-2)
ball.set_speed(2)

def draw_players():
    pygame.draw.rect(screen, TEAL, (player1.get_x(), player1.get_y(), player_width, player_height))
    pygame.draw.rect(screen, TEAL, (player2.get_x(), player2.get_y(), player_width, player_height))

def move_players():
    player1_y = player1.get_y()
    player2_y = player2.get_y()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= 300 * dt * player_speed
    if keys[pygame.K_s]:
        player1_y += 300 * dt * player_speed

    if keys[pygame.K_UP]:
        player2_y -= 300 * dt * player_speed
    if keys[pygame.K_DOWN]:
        player2_y += 300 * dt * player_speed

    player1.set_y(player1_y)
    player2.set_y(player2_y)

def draw_ball():
    pygame.draw.circle(screen, ball_color, (ball.get_x(), ball.get_y()), ball.get_radius())

def move_ball():
    ball_x = ball.get_x()
    ball_y = ball.get_y()
    ball_x += ball.get_dx() * ball.get_speed()
    ball_y += ball.get_dy() * ball.get_speed()
    ball.set_x(ball_x)
    ball.set_y(ball_y)

# game loop
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    draw_players()
    draw_ball()
    move_players()
    move_ball()

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(fps) / 1000

pygame.quit()
