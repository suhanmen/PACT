def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                result.append((i, j))
    result.sort()
    result.sort(key=lambda tup: tup[1], reverse=True)
    return result
