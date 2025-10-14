def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, j))
    
    coordinates.sort(key=lambda coord: coord[0])
    coordinates.sort(key=lambda coord: coord[1], reverse=True)
    
    return coordinates
