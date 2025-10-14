def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, j))
    
    # sort by rows in ascending order
    coordinates.sort(key=lambda tup: tup[0])
    
    # sort by columns in descending order within each row
    for i in range(len(coordinates)):
        row = lst[coordinates[i][0]]
        row_coordinates = [tup for tup in coordinates if tup[0] == i]
        row_coordinates.sort(key=lambda tup: tup[1], reverse=True)
        coordinates[i:i+len(row_coordinates)] = row_coordinates
    
    return coordinates
