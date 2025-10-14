def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, num in enumerate(row):
            if num == x:
                coordinates.append((i, j))
    coordinates = sorted(coordinates, key=lambda coord: coord[0])
    coordinates = sorted(coordinates, key=lambda coord: coord[1], reverse=True)
    return coordinates
