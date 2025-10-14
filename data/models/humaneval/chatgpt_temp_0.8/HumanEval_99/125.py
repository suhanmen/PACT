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
    # Convert the input string to a float
    value = float(value)

    # Round the float to the nearest integer
    rounded = round(value)

    # If the rounded value is equidistant from two integers, round away from zero
    if abs(value - rounded) == 0.5:
        if value > 0:
            return int(rounded + 0.5)
        else:
            return int(rounded - 0.5)

    # Otherwise, return the rounded value as an integer
    return int(rounded)
