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

    # Convert the string to a float
    num = float(value)

    # Check if the number is already an integer
    if num.is_integer():
        return int(num)

    # If not, calculate the distance to the nearest two integers
    lower_int = int(num)
    upper_int = lower_int + 1
    distance_lower = abs(num - lower_int)
    distance_upper = abs(num - upper_int)

    # Round away from zero if equidistant from two integers
    if distance_lower == distance_upper:
        if num > 0:
            return upper_int
        else:
            return lower_int * -1
    elif distance_lower < distance_upper:
        return lower_int
    else:
        return upper_int
