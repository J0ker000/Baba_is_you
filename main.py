import pygame
import sys


def load_texture():
    textures = {
        'Floore': (pygame.image.load('Textures/Floore.png'), []),
        'Baba': (pygame.image.load('Textures/Baba.png'), [7, 7])
    }
    return textures
def render(screen, textures):
    #Отрисовка пола грового поля
    for x in range(15):
        for y in range(15):
            screen.blit(textures['Floore'][0], (x*textures['Floore'][0].get_height(),
                                                y*textures['Floore'][0].get_width()))

    #Отрисовка всех оставшихся объктов
    for image in textures:
        if not image == 'Floore':
            screen.blit(textures[image][0], (textures[image][1][0]*textures[image][0].get_height(),
                                             textures[image][1][1]*textures[image][0].get_width()))
    pygame.display.flip()
def main():
    textures = load_texture()
    width = textures['Floore'][0].get_width()*15     # Ширина окна
    height = textures['Floore'][0].get_height()*15    # Высота окна (Поле: 15X15; Размер сектора = 50)
    pygame.init()
    FPS = 30
    clock =pygame.time.Clock()
    screen = pygame.display.set_mode([width, height])
    gameover = False
    while not gameover:
        #Обработка событий
        for event in pygame.event.get():
            #Выход из игры
            if event.type == pygame.QUIT:
                gameover = True

        render(screen, textures)
        clock.tick(FPS)
    sys.exit(0)

if __name__ == '__main__':
    main()