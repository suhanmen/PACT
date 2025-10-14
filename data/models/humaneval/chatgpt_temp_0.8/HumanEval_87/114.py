def get_row(lst, x):
    result = []
    for row_index, row in enumerate(lst):
        if x in row:
            for col_index, col in reversed(list(enumerate(row))):
                if col == x:
                    result.append((row_index, col_index))
    result.sort(key=lambda x: x[0])
    return result
