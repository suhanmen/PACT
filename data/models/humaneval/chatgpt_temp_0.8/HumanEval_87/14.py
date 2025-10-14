def get_row(lst, x):
    coordinates = []
    for row_idx, row in enumerate(lst):
        for col_idx, val in enumerate(row):
            if val == x:
                coordinates.append((row_idx, col_idx))
    coordinates.sort(key=lambda coord: coord[0])
    coordinates.sort(key=lambda coord: coord[1], reverse=True)
    return coordinates
