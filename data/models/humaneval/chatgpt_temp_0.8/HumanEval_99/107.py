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

    # Convert the string value to a float
    value = float(value)

    # Check if the absolute value of the input is already an integer
    if abs(value) == int(abs(value)):
        return int(value)

    # If the input is positive, round up to the nearest integer
    elif value > 0:
        return int(value + 0.5)

    # If the input is negative, round down to the nearest integer
    else:
        return int(value - 0.5)
