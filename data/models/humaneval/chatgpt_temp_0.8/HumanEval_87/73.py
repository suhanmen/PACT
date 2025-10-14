def get_row(lst, x):
    coords = []
    for row_idx, row in enumerate(lst):
        for col_idx, val in enumerate(row):
            if val == x:
                coords.append((row_idx, col_idx))
    coords.sort()
    coords.sort(key=lambda coord: coord[1], reverse=True)
    return coords
