def get_row(lst, x):
    result = []
    for row in range(len(lst)):
        if x in lst[row]:
            indices = [i for i, val in enumerate(lst[row]) if val == x]
            for col in sorted(indices, reverse=True):
                result.append((row, col))
    return sorted(result, key=lambda x: x[0])
