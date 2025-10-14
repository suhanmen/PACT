def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        row = lst[i]
        for j in range(len(row)):
            if row[j] == x:
                result.append((i, j))
    result.sort(key=lambda tup: tup[0])
    result.sort(key=lambda tup: tup[1], reverse=True)
    return result
