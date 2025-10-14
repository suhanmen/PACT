def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                coordinates.append((i, j))
    coordinates_sorted = sorted(coordinates, key=lambda x: (x[0], -x[1]))
    return coordinates_sorted
