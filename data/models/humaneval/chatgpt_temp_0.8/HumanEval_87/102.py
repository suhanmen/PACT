def get_row(lst, x):
    coordinates = []
    for row_idx, row in enumerate(lst):
        if x in row:
            for col_idx, col in enumerate(row):
                if col == x:
                    coordinates.append((row_idx, col_idx))
            coordinates.sort(key=lambda x: (-x[1]))
    coordinates.sort()
    return coordinates
