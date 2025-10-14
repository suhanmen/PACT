def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    result.append((i, j))
    result.sort(key=lambda x: x[0])
    for i in range(len(result)):
        row = result[i][0]
        sorted_row = sorted([r for r in result if r[0] == row], key=lambda x: x[1], reverse=True)
        result[i:i+len(sorted_row)] = sorted_row
    return result
