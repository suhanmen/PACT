def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        if x in lst[i]:
            j = len(lst[i]) - 1
            while j >= 0:
                if lst[i][j] == x:
                    result.append((i, j))
                j -= 1
    result.sort(key=lambda x: x[0])
    for i in range(len(result)):
        result[i] = (result[i][0], result[i][1])
    return result
