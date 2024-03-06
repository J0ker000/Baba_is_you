import pygame
import sys
from protocols import push_protocol, stop_protocol, collision_with_players_protocol
from render import render
from object import Object
def load_texture():
    floore = pygame.image.load('Textures/Floore.png')
    objects = {
        'Baba': Object(pygame.image.load('Textures/Baba.png'), [[7, 7], [1, 2]], False, False),
        'Wall': Object(pygame.image.load('Textures/Wall.png'), [[10, 10], [7, 8]], False, True)
    }
    return floore, objects
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
def move(shift, objects):
    object_coords = objects['Baba'].coords
    for player_coords in object_coords:
        player_coords[0] += shift[0]
        player_coords[1] += shift[1]
        #Коллизия объектов с границами карты
        if (max(player_coords) > 14) or (min(player_coords) < 0):
            stop_protocol(player_coords, shift)
    # Взаимодействие с объектами
    for index in objects:
        for player_coords in object_coords:
            if objects[index].stop:
                if player_coords in objects[index].coords:
                    stop_protocol(player_coords, shift)
            if objects[index].push:
                push_protocol(objects[index].coords, shift, player_coords, object_coords)
    collision_with_players_protocol(object_coords, shift)

def main():
    floore, objects = load_texture()
    width = floore.get_width()*15     # Ширина окна
    height = floore.get_height()*15    # Высота окна (Поле: 15X15; Размер сектора = 50)
    pygame.init()
    FPS = 30
    clock = pygame.time.Clock()
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
                move(management(event.key), objects)

        render(screen, floore, objects)
        pygame.display.flip()
        clock.tick(FPS)
    sys.exit(0)

if __name__ == '__main__':
    main()