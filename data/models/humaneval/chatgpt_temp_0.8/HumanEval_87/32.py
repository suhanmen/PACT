def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i,j))
    coordinates = sorted(coordinates, key=lambda x: x[0])
    for i in range(len(coordinates)):
        row = lst[coordinates[i][0]]
        coordinates[i] = (coordinates[i][0], coordinates[i][1], row[coordinates[i][1]])
    coordinates = sorted(coordinates, key=lambda x: (-x[0], -x[2]))
    return [(x[0], x[1]) for x in coordinates]
