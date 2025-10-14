def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    result.sort(key=lambda x: x[0])
    for i in range(len(result)):
        result[i] = (result[i][0], result[i][1])
    return result
