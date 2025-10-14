def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i,j))
    sorted_coordinates = sorted(coordinates, key=lambda x: x[0])
    for i in range(len(sorted_coordinates)):
        current_row = sorted_coordinates[i][0]
        row_coordinates = [coord for coord in sorted_coordinates if coord[0] == current_row]
        sorted_row_coordinates = sorted(row_coordinates, key=lambda x: x[1], reverse=True)
        sorted_coordinates[i:i+len(row_coordinates)] = sorted_row_coordinates
    return sorted_coordinates
