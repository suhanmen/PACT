def get_row(lst, x):
    coordinates = []
    for row_index, row in enumerate(lst):
        for col_index, val in enumerate(row):
            if val == x:
                coordinates.append((row_index, col_index))
    # sort coordinates by rows in ascending order
    coordinates.sort()
    # sort coordinates of the row by columns in descending order
    coordinates = sorted(coordinates, key=lambda x: x[1], reverse=True)
    return coordinates
