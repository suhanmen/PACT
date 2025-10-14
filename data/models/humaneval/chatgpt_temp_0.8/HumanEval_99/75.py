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
    num = float(value)

    # Get the integer part of the input number
    integer_part = int(num)

    # Check if the input number is equidistant from two integers
    if abs(num - integer_part) == 0.5:
        # If so, round it away from zero
        if num > 0:
            return int(num + 0.5)
        else:
            return int(num - 0.5)

    # Otherwise, round the input number to the nearest integer
    return round(num)
