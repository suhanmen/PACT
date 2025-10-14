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

    # If the value is negative, get its absolute value to make it positive
    if value < 0:
        value = abs(value)

    # Get the integer values that are closest to the given value
    lower_int = int(value)
    upper_int = lower_int + 1

    # Calculate the difference between the given value and the closest integers
    lower_diff = value - lower_int
    upper_diff = upper_int - value

    # If the difference to the lower integer is smaller or equal to
    # the difference to the upper integer, return the lower integer.
    # Otherwise, return the upper integer.
    if lower_diff <= upper_diff:
        return -lower_int if value < 0 else lower_int
    else:
        return -upper_int if value < 0 else upper_int
