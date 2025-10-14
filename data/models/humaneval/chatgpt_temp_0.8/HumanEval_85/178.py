def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Initialize the sum to zero
    total = 0
    # Iterate over odd indices in the list
    for i in range(1, len(lst), 2):
        # Check if the element at this index is even
        if lst[i] % 2 == 0:
            # Increment the sum by this element
            total += lst[i]
    # Return the sum
    return total
