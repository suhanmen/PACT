def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, num in enumerate(row):
            if num == x:
                coordinates.append((i, j))
    sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))
    return sorted_coordinates
