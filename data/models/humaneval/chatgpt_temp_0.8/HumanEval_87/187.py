def get_row(lst, x):
    row_col = []
    for i in range(len(lst)):
        if x in lst[i]:
            for j in range(len(lst[i])):
                if lst[i][j] == x:
                    row_col.append((i, j))
    row_col.sort(key=lambda x: x[0])
    row_col.sort(key=lambda x: x[1], reverse=True)
    return row_col
