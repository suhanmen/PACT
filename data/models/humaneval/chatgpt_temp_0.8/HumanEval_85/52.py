def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices."""
    sum = 0 # initialize sum to 0
    for i in range(1, len(lst), 2): # iterate through odd indices
        if lst[i] % 2 == 0: # check if element is even
            sum += lst[i] # add even element to sum
    return sum # return the sum of even elements at odd indices
