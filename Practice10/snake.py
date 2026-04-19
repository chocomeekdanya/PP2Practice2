import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

cell_size = 20
snake = [(100, 100)]
direction = (20, 0)

food = (random.randrange(0, WIDTH, cell_size),
        random.randrange(0, HEIGHT, cell_size))

score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 30)

def generate_food():
    while True:
        new_food = (random.randrange(0, WIDTH, cell_size),
                    random.randrange(0, HEIGHT, cell_size))
        if new_food not in snake:
            return new_food

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -20)
            if event.key == pygame.K_DOWN:
                direction = (0, 20)
            if event.key == pygame.K_LEFT:
                direction = (-20, 0)
            if event.key == pygame.K_RIGHT:
                direction = (20, 0)

    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Wall collision
    if (head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT):
        running = False

    # Self collision
    if head in snake:
        running = False

    snake.insert(0, head)

    # Food collision
    if head == food:
        score += 1
        food = generate_food()

        # Level system
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, cell_size, cell_size))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), (*food, cell_size, cell_size))

    # Score + level
    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
