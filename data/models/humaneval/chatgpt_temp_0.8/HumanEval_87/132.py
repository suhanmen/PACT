def get_row(lst, x):
    coords = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coords.append((i, j))
    coords.sort(key=lambda coord: (coord[0], -coord[1]))
    return coords
