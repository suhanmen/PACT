def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert number to string
    x_str = str(x)
    # get length of string
    length = len(x_str)
    # calculate effective shift by taking remainder
    shift = shift % length
    # check if effective shift is 0, return original string
    if shift == 0:
        return x_str
    # if shift is greater than length, reverse the string
    elif shift > length:
        return x_str[::-1]
    # otherwise, circularly shift the digits to the right
    else:
        shifted_str = x_str[length - shift:] + x_str[:length - shift]
        return shifted_str
