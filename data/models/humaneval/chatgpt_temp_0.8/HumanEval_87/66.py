def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            for j, val in sorted(enumerate(row), key=lambda x: -x[1]):
                if val == x:
                    result.append((i, j))
    return result
