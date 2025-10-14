def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        row = lst[i]
        if x in row:
            for j in range(len(row)):
                if row[j] == x:
                    coordinates.append((i, j))
    sorted_coordinates = sorted(coordinates, key=lambda x: (x[0], -x[1]))
    return sorted_coordinates
