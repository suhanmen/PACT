def get_row(lst, x):
    coordinates = []
    for row_idx in range(len(lst)):
        if x in lst[row_idx]:
            for col_idx in range(len(lst[row_idx])):
                if lst[row_idx][col_idx] == x:
                    coordinates.append((row_idx, col_idx))
    coordinates.sort(key=lambda coord: coord[0])
    coordinates.sort(key=lambda coord: -coord[1])
    return coordinates
