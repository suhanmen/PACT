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

    # convert value to float
    value = float(value)

    # find the integer that is closest to the given value
    closest_int = int(value + 0.5) if value > 0 else int(value - 0.5)

    # if the given value is equidistant from two integers, round away from zero
    if abs(value - closest_int + 0.5) == abs(value - closest_int - 0.5):
        closest_int += 1 if closest_int > 0 else -1

    return closest_int
