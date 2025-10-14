def get_row(lst, x):
    coordinates = []
    for row_index, row in enumerate(lst):
        for col_index, col_value in enumerate(row):
            if col_value == x:
                coordinates.append((row_index, col_index))
    coordinates.sort(key=lambda x: x[0])
    coordinates.sort(key=lambda x: x[1], reverse=True)
    return coordinates
