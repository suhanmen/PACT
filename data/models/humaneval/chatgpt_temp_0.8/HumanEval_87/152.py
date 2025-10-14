def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in reversed(list(enumerate(row))):
                if col == x:
                    coordinates.append((i, j))
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))
    return coordinates
