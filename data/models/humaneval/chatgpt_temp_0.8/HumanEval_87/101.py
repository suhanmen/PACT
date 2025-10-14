def get_row(lst, x):
    coordinates = []
    for row_idx, row in enumerate(lst):
        if x in row:
            for col_idx in sorted(range(len(row)), reverse=True):
                if row[col_idx] == x:
                    coordinates.append((row_idx, col_idx))
    return sorted(coordinates)
