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
    # Convert the input value (string) to a float
    value = float(value)
    
    # Get the floor and ceil of the input value
    floor_val = int(value - 0.5)
    ceil_val = int(value + 0.5)
    
    # Calculate the difference between the input value and the floor/ceil
    diff_floor = abs(value - floor_val)
    diff_ceil = abs(value - ceil_val)
    
    # Determine the closest integer and return it
    if diff_floor < diff_ceil:
        return floor_val
    elif diff_ceil < diff_floor:
        return ceil_val
    else:
        return ceil_val if ceil_val > 0 else floor_val
