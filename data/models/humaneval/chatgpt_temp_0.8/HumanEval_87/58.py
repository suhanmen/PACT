def get_row(lst, x):
    res = []
    # Iterate through each row of the list
    for i in range(len(lst)):
        # If x is present in the row
        if x in lst[i]:
            # Iterate through each index of the row
            for j in range(len(lst[i])):
                # If the index contains x, add it to the result list
                if lst[i][j] == x:
                    res.append((i, j))
    # Sort the result list by row in ascending order
    res.sort(key=lambda tup: tup[0])
    # Sort the result list by column in descending order
    res.sort(key=lambda tup: tup[1], reverse=True)
    return res
