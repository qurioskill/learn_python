import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Car Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Car settings
car_width, car_height = 50, 100
car = pygame.Rect(WIDTH//2 - car_width//2, HEIGHT - car_height - 10, car_width, car_height)
car_speed = 5

# Obstacle settings
obstacle_width, obstacle_height = 40, 40
obstacles = []
obstacle_timer = 0
obstacle_interval = 1500  # ms

# Font
font = pygame.font.SysFont(None, 48)

# Game state
prompt_displayed = False

def draw_car():
    pygame.draw.rect(screen, GREEN, car)

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

def show_prompt():
    prompt = font.render("STOP! Pedestrian ahead!", True, RED)
    screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, HEIGHT//2))

# Main game loop
running = True
while running:
    screen.fill(GRAY)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key Presses
    keys = pygame.key.get_pressed()
    if not prompt_displayed:
        if keys[pygame.K_LEFT] and car.left > 0:
            car.x -= car_speed
        if keys[pygame.K_RIGHT] and car.right < WIDTH:
            car.x += car_speed
        if keys[pygame.K_UP] and car.top > 0:
            car.y -= car_speed
        if keys[pygame.K_DOWN] and car.bottom < HEIGHT:
            car.y += car_speed

    # Generate obstacles
    if pygame.time.get_ticks() - obstacle_timer > obstacle_interval:
        x_pos = random.randint(0, WIDTH - obstacle_width)
        new_obstacle = pygame.Rect(x_pos, -obstacle_height, obstacle_width, obstacle_height)
        obstacles.append(new_obstacle)
        obstacle_timer = pygame.time.get_ticks()

    # Move obstacles
    for obstacle in obstacles:
        obstacle.y += 5

    # Check for collision
    for obstacle in obstacles:
        if car.colliderect(obstacle):
            prompt_displayed = True
            break

    draw_car()
    draw_obstacles()

    if prompt_displayed:
        show_prompt()

    pygame.display.flip()
    clock.tick(FPS)
