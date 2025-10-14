def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # Initialize the sum to zero
    sum = 0

    # Loop through the odd indices in the list
    for i in range(1, len(lst), 2):

        # Check if the element is even
        if lst[i] % 2 == 0:

            # Add the element to the sum
            sum += lst[i]

    # Return the sum
    return sum
