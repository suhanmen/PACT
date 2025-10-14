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

    # convert the input string to a float
    value = float(value)
    
    # if the value is already an integer, return it
    if value == int(value):
        return int(value)

    # if the value is positive, round up if decimal is >= 0.5, else round down
    if value > 0:
        if value - int(value) >= 0.5:
            return int(value) + 1
        else:
            return int(value)

    # if the value is negative, round up if decimal is <= -0.5, else round down
    else:
        if abs(value - int(value)) >= 0.5:
            return int(value) - 1
        else:
            return int(value)
