def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i, j))
    coordinates.sort(key=lambda tup: tup[0])
    coordinates.sort(key=lambda tup: tup[1], reverse=True)
    return coordinates
