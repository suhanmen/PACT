def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    # Define a function to check if a number has any even digit
    def has_even_digit(num):
        for digit in str(num):
            if int(digit) % 2 == 0:
                return True
        return False

    # Filter out the numbers with even digits
    filtered_list = list(filter(lambda num: not has_even_digit(num), x))

    # Sort the filtered list and return it
    return sorted(filtered_list)
