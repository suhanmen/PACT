def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert input integer to string
    x_str = str(x)

    # determine the length of the string
    length = len(x_str)

    # if shift is greater than the length of the string, reverse the string
    if shift >= length:
        return x_str[::-1]

    # otherwise, perform the circular shift
    shifted_str = x_str[-shift:] + x_str[:-shift]

    # return the shifted string
    return shifted_str
