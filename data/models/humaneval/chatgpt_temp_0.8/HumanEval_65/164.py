def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    len_x = len(str_x)
    if shift > len_x:
        return str_x[::-1]
    shifted_str = str_x[-shift:] + str_x[:-shift]
    return shifted_str
