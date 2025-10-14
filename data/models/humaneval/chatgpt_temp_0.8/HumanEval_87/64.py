def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i,j))
    coordinates = sorted(coordinates, key=lambda x: (x[0], -x[1]))
    return coordinates
