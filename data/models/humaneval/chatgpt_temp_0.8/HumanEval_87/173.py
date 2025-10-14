def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in sorted(enumerate(row), key=lambda c: -c[1]):
                if col == x:
                    coordinates.append((i, j))
    return coordinates
