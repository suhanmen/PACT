def get_row(lst, x):
    coords = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coords.append((i, j))
    coords = sorted(coords, key=lambda x: (x[0], -x[1]))
    return coords
