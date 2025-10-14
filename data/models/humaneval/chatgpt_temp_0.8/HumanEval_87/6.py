python
def get_row(lst, x):
    coords = []
    for row_idx, row in enumerate(lst):
        for col_idx, val in reversed(list(enumerate(row))):
            if val == x:
                coords.append((row_idx, col_idx))
    coords.sort()
    return coords
