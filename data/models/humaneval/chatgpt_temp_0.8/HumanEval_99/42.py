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

    # Convert the input string into a float
    value = float(value)

    # If the value is already an integer, return it
    if value == int(value):
        return int(value)

    # Find the two integers that the value is between
    lower = int(value)
    upper = lower + 1

    # Calculate the distances between the value and each integer
    distance_lower = value - lower
    distance_upper = upper - value

    # If the value is equidistant from the two integers, round away from zero
    if distance_lower == distance_upper:
        if value < 0:
            return lower
        else:
            return upper

    # Otherwise, return the closest integer
    elif distance_lower < distance_upper:
        return lower
    else:
        return upper
