def get_row(lst, x):
    res = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                res.append((i, j))
    res.sort(key=lambda tup: tup[0])
    res.sort(key=lambda tup: tup[1], reverse=True)
    return res
