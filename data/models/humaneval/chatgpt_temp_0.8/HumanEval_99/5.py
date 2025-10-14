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

    # Convert value to float
    value = float(value)

    # Check if value is already an integer
    if value.is_integer():
        return int(value)

    # Determine the two closest integers
    lower_int = int(value)
    upper_int = lower_int + 1

    # Calculate the distances from value to each integer
    lower_dist = value - lower_int
    upper_dist = upper_int - value

    # Return the closest integer
    if lower_dist < upper_dist:
        return lower_int
    elif upper_dist < lower_dist:
        return upper_int
    else: # If the distances are equal, round away from zero
        if value > 0:
            return upper_int
        else:
            return lower_int
