def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        if x in lst[i]:
            indices = [j for j, y in enumerate(lst[i]) if y == x]
            for idx in indices:
                coordinates.append((i, idx))
    coordinates.sort(key=lambda tup: (tup[0], -tup[1]))
    return coordinates
