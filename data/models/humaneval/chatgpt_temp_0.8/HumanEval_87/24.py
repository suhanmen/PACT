def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                coordinates.append((i, j))
    sorted_coordinates = sorted(coordinates, key=lambda c: c[0])
    return sorted(sorted_coordinates, key=lambda c: c[1], reverse=True)
