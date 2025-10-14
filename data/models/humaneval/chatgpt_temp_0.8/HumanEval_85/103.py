def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices."""
    total = 0 # initialize total to 0
    for i in range(1, len(lst), 2): # iterate through odd indices
        if lst[i] % 2 == 0: # check if element at odd index is even
            total += lst[i] # add even element to total
    return total # return the total sum of even elements at odd indices
