def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''

    # Convert the value to a float
    value = float(value)

    # Get the integer below and above the value
    lower_int = int(value)
    upper_int = lower_int + 1

    # Calculate the distances between the value and the two integers
    lower_dist = value - lower_int
    upper_dist = upper_int - value

    # If the distances are equal, round away from zero
    if lower_dist == upper_dist:
        return int(value + 0.5 * abs(value) / value)

    # Return the integer with the smallest distance
    return lower_int if lower_dist < upper_dist else upper_int
