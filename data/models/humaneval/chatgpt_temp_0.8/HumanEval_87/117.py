def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                coordinates.append((i, j))
    sorted_coordinates = sorted(coordinates, key=lambda x: x[0])
    for i in range(len(sorted_coordinates)):
        for j in range(i+1, len(sorted_coordinates)):
            if sorted_coordinates[j][0] == sorted_coordinates[i][0] and sorted_coordinates[j][1] > sorted_coordinates[i][1]:
                sorted_coordinates[i], sorted_coordinates[j] = sorted_coordinates[j], sorted_coordinates[i]
    return sorted_coordinates
