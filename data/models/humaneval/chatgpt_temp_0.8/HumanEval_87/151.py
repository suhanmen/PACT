def get_row(lst, x):
    coordinates = []
    for row_num, row in enumerate(lst):
        if x in row:
            for col_num, col in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if col == x:
                    coordinates.append((row_num, col_num))
    return sorted(coordinates)
