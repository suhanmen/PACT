def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            col_indices = [j for j, val in enumerate(row) if val == x]
            for col in sorted(col_indices, reverse=True):
                result.append((i, col))
    result.sort()
    return result
