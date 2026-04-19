import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'brush'   # brush, rect, circle, eraser
    color = (0, 0, 255)

    points = []

    drawing = False
    start_pos = None

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                # Modes
                if event.key == pygame.K_1:
                    mode = 'brush'
                elif event.key == pygame.K_2:
                    mode = 'rect'
                elif event.key == pygame.K_3:
                    mode = 'circle'
                elif event.key == pygame.K_4:
                    mode = 'eraser'

                # Colors
                elif event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                end_pos = event.pos

                if mode == 'rect':
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, rect, 2)

                elif mode == 'circle':
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    radius_circle = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius_circle, 2)

            if event.type == pygame.MOUSEMOTION:
                if drawing and mode == 'brush':
                    points.append(event.pos)
                    points = points[-256:]

                elif drawing and mode == 'eraser':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        # Draw brush lines
        if mode == 'brush':
            for i in range(len(points) - 1):
                drawLineBetween(screen, i, points[i], points[i + 1], radius, color)

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations if iterations != 0 else 0
        x = int(start[0] + (end[0] - start[0]) * progress)
        y = int(start[1] + (end[1] - start[1]) * progress)
        pygame.draw.circle(screen, color, (x, y), width)


main()
