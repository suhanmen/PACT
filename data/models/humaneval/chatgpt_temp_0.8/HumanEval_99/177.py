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

    # First, convert the input string to a float
    value = float(value)

    # Check if the value is already an integer
    if value.is_integer():
        return int(value)

    # If not, find the closest integer by rounding the value
    closest_int = round(value)

    # If the rounded value is greater than the original value,
    # and the difference between the two is exactly 0.5, round up
    if closest_int > value and closest_int - value == 0.5:
        return int(closest_int)

    # If the rounded value is less than the original value,
    # and the difference between the two is exactly 0.5, round down
    elif closest_int < value and value - closest_int == 0.5:
        return int(closest_int)

    # Otherwise, return the rounded value
    else:
        return int(closest_int)
