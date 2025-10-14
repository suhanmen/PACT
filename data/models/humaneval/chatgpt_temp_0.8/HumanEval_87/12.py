def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, num in enumerate(row):
            if num == x:
                result.append((i, j))
    result.sort(key=lambda x: x[0]) # sort by row
    result.sort(key=lambda x: x[1], reverse=True) # sort by column in descending order
    return result
