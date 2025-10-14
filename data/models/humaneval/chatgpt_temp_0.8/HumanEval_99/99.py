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

    # Convert value to float
    value_float = float(value)

    # Check if the absolute value of the decimal part is greater or equal to 0.5
    if abs(value_float % 1) >= 0.5:
        # Round up if the number is positive, else round down
        if value_float >= 0:
            return int(value_float) + 1
        else:
            return int(value_float) - 1
    else:
        # Round down if the number is positive, else round up
        if value_float >= 0:
            return int(value_float)
        else:
            return int(value_float)
