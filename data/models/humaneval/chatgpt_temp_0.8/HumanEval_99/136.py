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

    # Convert the input value to a float
    value = float(value)

    # Check if the number is already an integer
    if value.is_integer():
        return int(value)

    # Calculate the distance to the nearest integer both below and above the given number 
    distance_below = value - int(value)
    distance_above = 1 - distance_below

    # Handle the special case of values exactly halfway between two integers
    if distance_below == distance_above:
        # Round away from zero
        if value >= 0:
            return int(value + 0.5)
        else:
            return int(value - 0.5)

    # Return the closest integer
    if distance_below < distance_above:
        return int(value)
    else:
        return int(value + 1)
