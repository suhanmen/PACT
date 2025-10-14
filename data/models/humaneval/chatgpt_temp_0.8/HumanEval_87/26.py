def get_row(lst, x):
    coords = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coords.append((i, j))
    coords.sort(key=lambda x: x[0])
    for row in coords:
        lst[row[0]].sort(reverse=True)
    return coords
