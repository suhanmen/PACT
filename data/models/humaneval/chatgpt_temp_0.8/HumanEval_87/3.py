def get_row(lst, x):
    coords = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in reversed(list(enumerate(row))):
                if col == x:
                    coords.append((i, j))
    coords.sort()
    return coords
