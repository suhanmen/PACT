def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        if x in row:
            for j, column in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if column == x:
                    coordinates.append((i, j))
    return sorted(coordinates)
