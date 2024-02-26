import pygame
import sys

def main():
    width = 700     # Ширина окна
    height = 500    # Высота окна
    pygame.init()
    FPS = 30
    clock =pygame.time.Clock()
    screen = pygame.display.set_mode([width, height])
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

        screen.fill('white')
        pygame.display.flip()
        clock.tick(FPS)
    sys.exit(0)

if __name__ == '__main__':
    main()