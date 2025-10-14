def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i, j))
    coordinates = sorted(coordinates, key=lambda x: x[0])
    for i in range(len(coordinates)):
        row = lst[coordinates[i][0]]
        row_coordinates = sorted([(coordinates[i][0], j) for j in range(len(row)) if row[j] == x], key=lambda x: x[1], reverse=True)
        coordinates = coordinates[:i] + row_coordinates + coordinates[i+1:]
    return coordinates
