import pygame
import sys


def load_texture():
    objects = {
        'Floore': (pygame.image.load('Textures/Floore.png'), []),
        'Baba': (pygame.image.load('Textures/Baba.png'), [7, 7])
    }
    return objects
def render(screen, objects):
    #Отрисовка пола грового поля
    for x in range(15):
        for y in range(15):
            screen.blit(objects['Floore'][0], (x*objects['Floore'][0].get_height(),
                                                y*objects['Floore'][0].get_width()))

    #Отрисовка всех оставшихся объктов
    for image in objects:
        if not image == 'Floore':
            screen.blit(objects[image][0], (objects[image][1][0]*objects[image][0].get_height(),
                                             objects[image][1][1]*objects[image][0].get_width()))
    pygame.display.flip()
def management(key):
    if (key == pygame.K_w) or (key == pygame.K_UP):
        return (0, -1)
    if (key == pygame.K_s) or (key == pygame.K_DOWN):
        return (0, 1)
    if (key == pygame.K_a) or (key == pygame.K_LEFT):
        return (-1, 0)
    if (key == pygame.K_d) or (key == pygame.K_RIGHT):
        return (1, 0)
    return (0, 0)
def move(object_coords, shift):
    print(shift)
    object_coords[0] += shift[0]
    object_coords[1] += shift[1]
def main():
    objects = load_texture()
    width = objects['Floore'][0].get_width()*15     # Ширина окна
    height = objects['Floore'][0].get_height()*15    # Высота окна (Поле: 15X15; Размер сектора = 50)
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
            #Управление
            if event.type == pygame.KEYUP:
                move(objects['Baba'][1], management(event.key))

        render(screen, objects)
        clock.tick(FPS)
    sys.exit(0)

if __name__ == '__main__':
    main()