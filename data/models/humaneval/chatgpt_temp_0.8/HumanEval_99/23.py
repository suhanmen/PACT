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

    # Convert string value to float
    value = float(value)

    # Check if the value is already an integer
    if value.is_integer():
        return int(value)

    # Calculate the distance between the value and the two nearest integers
    lower_int = int(value)
    upper_int = lower_int + 1
    lower_dist = value - lower_int
    upper_dist = upper_int - value

    # Round away from zero if the distance to both integers is the same
    if lower_dist == upper_dist:
        return upper_int if value > 0 else lower_int

    # Return the closest integer
    return upper_int if upper_dist < lower_dist else lower_int
