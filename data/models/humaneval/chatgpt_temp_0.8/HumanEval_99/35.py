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

    # check if value is already an integer
    if value.is_integer():
        return int(value)

    # otherwise find the two closest integers
    lower_int = int(value)
    upper_int = lower_int + 1

    # check which integer is closer
    if abs(value - lower_int) < abs(value - upper_int):
        return lower_int
    elif abs(value - lower_int) > abs(value - upper_int):
        return upper_int
    else:
        # if the value is equidistant from two integers, round it away from zero
        if value < 0:
            return lower_int
        else:
            return upper_int
