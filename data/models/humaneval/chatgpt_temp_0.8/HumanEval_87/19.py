def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, col in reversed(list(enumerate(row))):
            if col == x:
                result.append((i, j))
    result.sort()
    return result
