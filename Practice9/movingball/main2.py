import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
radius = 25
step = 20

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if ball_x - step - radius >= 0:
                    ball_x -= step

            elif event.key == pygame.K_RIGHT:
                if ball_x + step + radius <= WIDTH:
                    ball_x += step

            elif event.key == pygame.K_UP:
                if ball_y - step - radius >= 0:
                    ball_y -= step

            elif event.key == pygame.K_DOWN:
                if ball_y + step + radius <= HEIGHT:
                    ball_y += step

    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
