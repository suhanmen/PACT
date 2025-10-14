def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Initialize sum to zero
    sum = 0 
    # Loop through the list, starting at index 1 and incrementing by 2
    for i in range(1, len(lst), 2):
        # Check if element at index i is even
        if lst[i] % 2 == 0:
            # Add the element to the sum
            sum += lst[i]
    return sum
