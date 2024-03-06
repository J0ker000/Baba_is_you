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