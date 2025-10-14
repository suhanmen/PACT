def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_str = str(x)
    n = len(x_str)
    shift = shift % n
    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        if shift > n:
            return shifted_str[::-1]
        else:
            return shifted_str
