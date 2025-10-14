def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            indices = [(i, j) for j, val in enumerate(row) if val == x]
            indices.sort(key=lambda tup: tup[1], reverse=True) # sort by columns in descending order
            result.extend(indices)
    result.sort() # sort by rows in ascending order
    return result
