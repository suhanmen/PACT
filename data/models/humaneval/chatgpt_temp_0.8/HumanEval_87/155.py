def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        if x in lst[i]:
            indices = [j for j in range(len(lst[i])) if lst[i][j] == x]
            for index in indices:
                result.append((i, index))
    result.sort(key=lambda tup: tup[0])
    result.sort(key=lambda tup: tup[1], reverse=True)
    return result
