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
    
    # Convert the value to a float
    value = float(value)
    
    # Round the value to the nearest integer
    rounded = round(value)
    
    # Check if the rounded value is greater or less than the original value
    if rounded > value:
        # If the rounded value is greater than the original value,
        # return the floor of the value (i.e. the closest integer that is less than the value)
        return int(value // 1)
    elif rounded < value:
        # If the rounded value is less than the original value,
        # return the ceiling of the value (i.e. the closest integer that is greater than the value)
        return int(value // 1 + 1)
    else:
        # If the rounded value is equal to the original value, return it as an integer
        return int(rounded)
