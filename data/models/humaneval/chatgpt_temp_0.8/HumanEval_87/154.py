def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        row = lst[i]
        if x in row:
            for j in range(len(row)):
                if row[j] == x:
                    coordinates.append((i, j))
    coordinates.sort(key=lambda x: x[0])
    coordinates.sort(key=lambda x: x[1], reverse=True)
    return coordinates
