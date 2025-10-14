def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result = sorted(result, key=lambda x: x[0])
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result
