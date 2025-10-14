def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, col in reversed(list(enumerate(row))):
            if col == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda c: c[0])
    return coordinates
