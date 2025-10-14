Here's the completed code:

def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda x: x[0])
    coordinates.sort(key=lambda x: x[1], reverse=True)
    return coordinates
