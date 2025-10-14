def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total = 0
    for i in range(1, len(lst), 2): # Only look at elements at odd indices
        if lst[i] % 2 == 0: # If the element is even
            total += lst[i] # Add it to the total
    return total
