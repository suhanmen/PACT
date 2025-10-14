def get_row(lst, x):
    results = []
    for row_idx, row in enumerate(lst):   
        for col_idx, val in enumerate(row):
            if val == x:
                results.append((row_idx, col_idx))
    results.sort(key=lambda x: x[0])
    results.sort(key=lambda x: x[1], reverse=True)
    return results
