def get_row(lst, x):
    res = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    res.append((i, j))
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1], reverse=True)
    return res
