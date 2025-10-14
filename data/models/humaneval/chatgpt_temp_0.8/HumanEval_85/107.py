def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # initialize sum to 0
    sum = 0
    
    # iterate over the list starting from the second element (index 1)
    for i in range(1,len(lst), 2):
        # check if the element at the current index is even
        if lst[i] % 2 == 0:
            # add it to the sum
            sum += lst[i]
    
    # return the sum
    return sum
