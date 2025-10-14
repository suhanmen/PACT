python
def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        if x in lst[i]:
            col_indices = [j for j in range(len(lst[i])) if lst[i][j] == x]
            for col in sorted(col_indices, reverse=True):
                result.append((i, col))
    return result
