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
def stop_protocol(coords, shift):
        coords[0] -= shift[0]
        coords[1] -= shift[1]
def collision_with_players_protocol(object_coords, shift):
    for coords in object_coords:
        if object_coords.count(coords) >= 2:
            coords[0] -= shift[0]
            coords[1] -= shift[1]