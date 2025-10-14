def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        row = lst[i]
        if x in row:
            for j in range(len(row)):
                if row[j] == x:
                    result.append((i, j))
            result.sort(key=lambda x: -x[1])
    result.sort()
    return result
