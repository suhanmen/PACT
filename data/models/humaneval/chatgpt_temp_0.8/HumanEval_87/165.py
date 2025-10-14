def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            indices = [(i, j) for j, val in sorted(enumerate(row), key=lambda x: -x[1]) if val == x]
            result.extend(indices)
    return sorted(result)
