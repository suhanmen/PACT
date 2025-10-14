def get_row(lst, x):
    coords = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    coords.sort(key=lambda c: c[0])
    coords.sort(key=lambda c: c[1], reverse=True)
    return coords
