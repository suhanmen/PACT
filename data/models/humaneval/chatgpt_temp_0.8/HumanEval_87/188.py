def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                result.append((i, j))
    # Sort coordinates initially by rows in ascending order
    result.sort(key=lambda tup: tup[0])
    # Sort coordinates of the row by columns in descending order
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[i][0] == result[j][0] and result[i][1] < result[j][1]:
                result[i], result[j] = result[j], result[i]
    return result
