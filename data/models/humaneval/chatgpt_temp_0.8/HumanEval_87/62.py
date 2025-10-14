def get_row(lst, x):
    res = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                res.append((i,j))
    res.sort(key=lambda tup: (tup[0], -tup[1]))
    return res
