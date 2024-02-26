import pygame
import sys


def load_texture():
    textures = {
        'Floore': pygame.image.load('Textures/Floore.png'),
        'Baba': pygame.image.load('Textures/Baba.png')
    }
    return textures
def main():
    textures = load_texture()
    width = textures['Floore'].get_width()*15     # Ширина окна
    height = textures['Floore'].get_height()*15    # Высота окна (Поле: 15X15; Размер сектора = 50)
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
        screen.blit(textures['Floore'], [0, 0])
        screen.blit(textures['Baba'], [150, 100])
        pygame.display.flip()
        clock.tick(FPS)
    sys.exit(0)

if __name__ == '__main__':
    main()