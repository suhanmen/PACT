python
def get_row(lst, x):
    row_coords = []
    for i, row in enumerate(lst):
        if x in row:
            for j, val in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if val == x:
                    row_coords.append((i, j))
    return sorted(row_coords, key=lambda x: x[0])
