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
    if "." not in value:
        return int(value)

    integer_part, decimal_part = value.split(".")
    integer_part = int(integer_part)
    decimal_part = int(decimal_part)

    if decimal_part == 0:
        return integer_part

    lower = integer_part
    upper = integer_part + 1

    if decimal_part < 0.5:
        return lower
    elif decimal_part > 0.5:
        return upper
    else:
        # Decimal part is exactly 0.5
        if integer_part >= 0:
            return upper
        else:
            return lower
