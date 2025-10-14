def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, j))
    coordinates.sort()
    coordinates = [(row, col) for row, col in coordinates if row != -1]
    return coordinates
