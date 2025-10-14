def get_row(lst, x):
    result = []
    for row_idx, row in enumerate(lst):
        if x in row:
            col_indices = [i for i, val in enumerate(row) if val == x]
            for col_idx in sorted(col_indices, reverse=True):
                result.append((row_idx, col_idx))
    result.sort()
    return result
