def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i, j))
    coordinates.sort(key=lambda x: x[0])
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            if coordinates[i][0] == coordinates[j][0] and coordinates[i][1] < coordinates[j][1]:
                coordinates[i], coordinates[j] = coordinates[j], coordinates[i]
    return coordinates
