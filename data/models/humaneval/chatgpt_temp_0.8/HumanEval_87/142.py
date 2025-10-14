def get_row(lst, x):
    coords = []
    for i, row in enumerate(lst):
        if x in row:
            for j, value in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if value == x:
                    coords.append((i, j))
    return sorted(coords)
