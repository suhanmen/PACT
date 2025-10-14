def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coordinates.append((i,j))
    sorted_coordinates = sorted(coordinates, key=lambda c: c[0])
    final_coordinates = sorted(sorted_coordinates, key=lambda c: c[1], reverse=True)
    return final_coordinates
