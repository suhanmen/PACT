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

    # Convert the string value to a float
    value = float(value)

    # Check if the value is already an integer
    if value.is_integer():
        return int(value)

    # Calculate the absolute difference between the value and its floor and ceiling
    diff_floor = abs(value - int(value))
    diff_ceil = abs(value - int(value) - 1)

    # Check which integer is closer and return it
    if diff_floor < diff_ceil:
        return int(value)
    else:
        return int(value) + 1 if value > 0 else int(value) - 1
