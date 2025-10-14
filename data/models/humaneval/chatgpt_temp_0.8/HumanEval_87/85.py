def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        if x in row:
            for j, val in sorted(enumerate(row), key=lambda k: k[1], reverse=True):
                if val == x:
                    coordinates.append((i, j))
    return sorted(coordinates)
