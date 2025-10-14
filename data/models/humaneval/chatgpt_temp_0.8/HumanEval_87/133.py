def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda x: x[0])
    coordinates.sort(key=lambda x: x[1], reverse=True)
    return coordinates
