def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i, j))
    sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))
    return sorted_coordinates
