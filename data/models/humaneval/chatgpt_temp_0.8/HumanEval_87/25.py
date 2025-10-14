def get_row(lst, x):
    result = []
    for i in range(len(lst)): # iterate over each row in the list
        if x in lst[i]: # if x is present in the row
            indices = [j for j, val in enumerate(lst[i]) if val == x] # get the indices of all occurrences of x
            for index in indices:
                result.append((i, index)) # append the coordinate tuple to the result list
    result.sort() # sort the result list by rows in ascending order
    result.sort(key=lambda x: x[1], reverse=True) # sort the result list by columns in descending order
    return result
