def get_row(lst, x):
    coords = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in sorted(enumerate(row), key=lambda x: -x[1]):
                if col == x:
                    coords.append((i, j))
    return coords
