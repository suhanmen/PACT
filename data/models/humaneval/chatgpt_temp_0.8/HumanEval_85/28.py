def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list starting from the second index
    for i in range(1, len(lst), 2):
        # Check if the element at the current index is even
        if lst[i] % 2 == 0:
            # Add the element to the total
            total += lst[i]

    # Return the total sum
    return total
