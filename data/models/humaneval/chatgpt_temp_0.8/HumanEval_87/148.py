def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coordinates.append((i, j))
    coordinates.sort()
    sorted_coordinates = []
    for row, col in coordinates:
        sorted_coordinates.append((row, col))
    return sorted_coordinates
