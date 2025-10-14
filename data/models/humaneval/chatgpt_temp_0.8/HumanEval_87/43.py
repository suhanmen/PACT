def get_row(lst, x):
    results = []
    for row_index, row in enumerate(lst):
        if x in row:
            for col_index, val in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
                if val == x:
                    results.append((row_index, col_index))
    return sorted(results)
