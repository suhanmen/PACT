def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            for j, col in reversed(list(enumerate(row))):
                if col == x:
                    result.append((i, j))
    return sorted(result)
