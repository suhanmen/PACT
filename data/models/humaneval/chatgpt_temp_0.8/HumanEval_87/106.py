def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        for j, num in enumerate(row):
            if num == x:
                res.append((i, j))
                
    res.sort(key=lambda tup: (tup[0], -tup[1]))
    return res
