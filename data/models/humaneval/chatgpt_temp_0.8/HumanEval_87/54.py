def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if col == x:
                    coordinates.append((i, j))
    return sorted(coordinates)
