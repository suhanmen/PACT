def get_row(lst, x):
    coords = []
    for row_idx, row in enumerate(lst):
        if x in row:
            for col_idx, col_val in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if col_val == x:
                    coords.append((row_idx, col_idx))
    coords.sort()
    return coords
