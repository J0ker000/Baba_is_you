def push_protocol(object_coords, shift, player_coords, all_players_coords):
    is_push = False
    for image_coords in object_coords:
        if image_coords == player_coords:
            is_push = True
            image_coords[0] += shift[0]
            image_coords[1] += shift[1]
    for i in range(len(object_coords)):
        for image_coords in object_coords:
            if object_coords.count(image_coords) >= 2:
                image_coords[0] += shift[0]
                image_coords[1] += shift[1]

    #Нужно запускать если передвигаемый объект упёрся в непередвигаемый объект(игрока)
    if is_push:
        for i in range(len(object_coords)):
            for image_coords in object_coords:
                #1. Если упирается в другого игорока 2. Если упирается в границу карты 3. Если упирается в такой же объект
                if ((image_coords in all_players_coords) and (not image_coords == player_coords)) or\
                        ((max(image_coords) > 14) or (min(image_coords) < 0)) or\
                        (object_coords.count(image_coords) >= 2):
                    image_coords[0] -= shift[0]
                    image_coords[1] -= shift[1]
                if image_coords == player_coords:
                    player_coords[0] -= shift[0]
                    player_coords[1] -= shift[1]
def stop_protocol(coords, shift):
        coords[0] -= shift[0]
        coords[1] -= shift[1]
def collision_with_players_protocol(object_coords, shift):
    for coords in object_coords:
        if object_coords.count(coords) >= 2:
            coords[0] -= shift[0]
            coords[1] -= shift[1]