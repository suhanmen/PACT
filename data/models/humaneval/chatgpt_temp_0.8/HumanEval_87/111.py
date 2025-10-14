def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in reversed(list(enumerate(row))):
                if col == x:
                    res.append((i, j))
    res.sort()
    return res
