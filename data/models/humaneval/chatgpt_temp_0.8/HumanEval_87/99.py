def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    coordinates.append((i, j))
    coordinates.sort(key=lambda x: x[0]) # sort by row in ascending order
    coordinates.sort(key=lambda x: x[1], reverse=True) # sort by column in descending order
    return coordinates
