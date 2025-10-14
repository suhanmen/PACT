def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # initialize the sum to zero
    total = 0
    
    # iterate over the list starting at the second element (index 1)
    for i in range(1, len(lst), 2):
        # if the element is even, add it to the total
        if lst[i] % 2 == 0:
            total += lst[i]
    
    return total
