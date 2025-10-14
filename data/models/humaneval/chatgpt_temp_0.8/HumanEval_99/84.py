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

    # Check if the number is already an integer
    if value.is_integer():
        return int(value)

    # If the number is not an integer, calculate the two closest integers
    lower_int = int(value)
    upper_int = lower_int + 1

    # Check which integer is closer to the input number
    if value - lower_int < upper_int - value:
        return lower_int
    elif value - lower_int > upper_int - value:
        return upper_int
    else:
        # If the input number is equidistant from two integers, round away from zero
        if value >= 0:
            return upper_int
        else:
            return lower_int
