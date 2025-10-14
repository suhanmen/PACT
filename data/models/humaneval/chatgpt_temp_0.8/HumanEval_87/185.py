def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in sorted([(i, k) for k in range(len(lst[i])) if lst[i][k] == x], key=lambda tup:(tup[0], -tup[1])):
                result.append(j)
    return result
