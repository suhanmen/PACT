def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, j))
    # Sort coordinates by rows in ascending order
    coordinates.sort(key=lambda c: c[0])
    # Sort coordinates of each row by columns in descending order
    for i in range(len(coordinates)-1, 0, -1):
        if coordinates[i][0] == coordinates[i-1][0]:
            if coordinates[i][1] > coordinates[i-1][1]:
                coordinates[i], coordinates[i-1] = coordinates[i-1], coordinates[i]
    return coordinates
