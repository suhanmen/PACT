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
    num = float(value)

    # Check if the absolute value of the number is closer to the next
    # integer or the previous integer, and round away from zero in that
    # direction
    if abs(num - int(num)) < 0.5:
        return int(num)
    elif num > 0:
        return int(num) + 1
    else:
        return int(num) - 1
