def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            for j, value in sorted([(j, v) for j, v in enumerate(row) if v == x], key=lambda x: -x[1]):
                result.append((i, j))
    return result
