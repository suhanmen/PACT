def get_row(lst, x):
    coords = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                coords.append((i, j))
    coords.sort(key=lambda x: x[0])
    coords.sort(key=lambda x: x[1], reverse=True)
    return coords
