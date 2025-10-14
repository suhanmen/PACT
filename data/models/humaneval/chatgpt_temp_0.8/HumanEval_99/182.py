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
    
    # Get the two integers closest to the value
    lower = int(value)
    upper = lower + 1
    
    # Check which integer is closer to the value
    if value - lower < upper - value:
        return lower
    elif value - lower > upper - value:
        return upper
    else:
        # If the value is equidistant from both integers, round away from zero
        if value < 0:
            return lower
        else:
            return upper
