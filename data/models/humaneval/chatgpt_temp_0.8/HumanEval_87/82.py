def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if col == x:
                    res.append((i, j))
    res.sort()
    return res
