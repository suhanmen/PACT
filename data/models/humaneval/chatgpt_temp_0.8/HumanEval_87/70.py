def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in enumerate(row):
                if col == x:
                    coordinates.append((i, j))
    sorted_coordinates = sorted(coordinates, key=lambda x: x[0])
    return sorted(sorted_coordinates, key=lambda x: x[1], reverse=True)
