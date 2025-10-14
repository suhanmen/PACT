def get_row(lst, x):
    result = []
    for row in range(len(lst)):
        if x in lst[row]:
            for col in sorted([(i, lst[row][i]) for i in range(len(lst[row])) if lst[row][i] == x], key=lambda x: x[1], reverse=True):
                result.append((row, col[0]))
    return result
