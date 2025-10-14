def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                coordinates.append((i, j))
    coordinates.sort()
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            if coordinates[i][0] == coordinates[j][0] and coordinates[i][1] < coordinates[j][1]:
                coordinates[i], coordinates[j] = coordinates[j], coordinates[i]
    return coordinates
