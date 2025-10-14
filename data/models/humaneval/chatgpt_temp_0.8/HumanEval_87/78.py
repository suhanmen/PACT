python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, item in enumerate(row):
            if item == x:
                result.append((i, j))
    result.sort(key=lambda coord: coord[0])
    result.sort(key=lambda coord: coord[1], reverse=True)
    return result
