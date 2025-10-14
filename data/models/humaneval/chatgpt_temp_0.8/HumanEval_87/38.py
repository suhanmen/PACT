def get_row(lst, x):
    result = []
    for row_num, row in enumerate(lst):
        if x in row:
            for col_num, col in reversed(list(enumerate(row))):
                if col == x:
                    result.append((row_num, col_num))
    result.sort(key=lambda x: x[0])
    return result
