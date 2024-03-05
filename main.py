import pygame
import sys

class Object:
    def __init__(self, image, coords, stop, push):
        self.image = image
        self.coords = coords
        self.stop = stop
        self.push = push
def load_texture():
    floore = pygame.image.load('Textures/Floore.png')
    objects = {
        'Baba': Object(pygame.image.load('Textures/Baba.png'), [[7, 7], [1, 2]], False, False),
        'Wall': Object(pygame.image.load('Textures/Wall.png'), [[10, 10], [7, 8]], False, True)
    }
    return floore, objects
def push_protocol(object_coords, shift, coords):
    for image_coords in object_coords:
        if image_coords == coords:
            image_coords[0] += shift[0]
            image_coords[1] += shift[1]
    for i in range(len(object_coords)):
        for coords in object_coords:
            if object_coords.count(coords) >= 2:
                coords[0] += shift[0]
                coords[1] += shift[1]
    return object_coords
def stop_protocol(coords, shift):
        coords[0] -= shift[0]
        coords[1] -= shift[1]
def render(screen, floore, objects):
    #Отрисовка пола грового поля
    for x in range(15):
        for y in range(15):
            screen.blit(floore, (x*floore.get_height(),
                                 y*floore.get_width()))

    #Отрисовка всех оставшихся объктов
    for object in objects:
        for coords in objects[object].coords:
            screen.blit(objects[object].image, [objects[object].image.get_height()*i for i in coords])

    pygame.display.flip()
def management(key):
    if (key == pygame.K_w) or (key == pygame.K_UP):
        return [0, -1]
    if (key == pygame.K_s) or (key == pygame.K_DOWN):
        return [0, 1]
    if (key == pygame.K_a) or (key == pygame.K_LEFT):
        return [-1, 0]
    if (key == pygame.K_d) or (key == pygame.K_RIGHT):
        return [1, 0]
    return [0, 0]
def move(object_coords, shift, objects):
    for coords in object_coords:
        coords[0] += shift[0]
        coords[1] += shift[1]
        #Коллизия объектов с границами карты
        if (max(coords) > 14) or (min(coords) < 0):
            stop_protocol(coords, shift)

        #Взаимодействие с объектами
        for index in objects:
            if objects[index].stop:
                if coords in objects[index].coords:
                    stop_protocol(coords, shift)

            if objects[index].push:
                objects[index].coords = push_protocol(objects[index].coords, shift, coords)

def main():
    floore, objects = load_texture()
    width = floore.get_width()*15     # Ширина окна
    height = floore.get_height()*15    # Высота окна (Поле: 15X15; Размер сектора = 50)
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
                move(objects['Baba'].coords, management(event.key), objects)

        render(screen, floore, objects)
        clock.tick(FPS)
    sys.exit(0)

if __name__ == '__main__':
    main()