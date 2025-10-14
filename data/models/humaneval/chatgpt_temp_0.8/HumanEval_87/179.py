def get_row(lst, x):
    result = []
    for row_idx, row in enumerate(lst):
        if x in row:
            for col_idx, col in enumerate(row):
                if col == x:
                    result.append((row_idx, col_idx))
    result = sorted(result, key=lambda x: (x[0], -x[1]))
    return result
