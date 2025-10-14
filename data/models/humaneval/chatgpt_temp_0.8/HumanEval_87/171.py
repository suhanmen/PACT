def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in enumerate(row):
                if col == x:
                    result.append((i, j))
    result.sort(key=lambda tup: tup[0])
    for i in range(len(result)):
        for j in range(i, len(result)):
            if result[i][0] == result[j][0] and result[i][1] < result[j][1]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    return result
