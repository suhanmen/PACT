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

    # First, convert the input value to a float
    num = float(value)

    # Check if the number is already an integer
    if num.is_integer():
        return int(num)

    # If the number is positive, round up if the decimal part is >= 0.5
    if num > 0:
        if num % 1 >= 0.5:
            return int(num) + 1
        else:
            return int(num)

    # If the number is negative, round down if the decimal part is <= -0.5
    else:
        if num % 1 <= -0.5:
            return int(num) - 1
        else:
            return int(num)
