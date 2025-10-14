def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..
    
    Args:
        lst (list): A non-empty list of integers
    
    Returns:
        int: The sum of even elements that are at odd indices in the input list

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Initialize the sum to zero
    total = 0
    
    # Loop through the list, starting from index 1 (which is odd)
    for i in range(1, len(lst), 2):
        # Check if the element at this index is even
        if lst[i] % 2 == 0:
            # Add it to the total
            total += lst[i]
    
    # Return the total
    return total
