def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = 0
    for i in range(1, len(lst), 2): # Loop through odd indices
        if lst[i] % 2 == 0: # Check if element at odd index is even
            result += lst[i] # Add even element to result
    return result
