def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # Initialize a variable to store the sum of even elements at odd indices
    sum_even_odd_indices = 0

    # Loop through the list and check if the element is even and its index is odd
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            sum_even_odd_indices += lst[i]

    # Return the sum of even elements at odd indices
    return sum_even_odd_indices
