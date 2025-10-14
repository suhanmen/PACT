def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_str = str(x)
    num_len = len(num_str)
    if shift >= num_len:
        return num_str[::-1]
    else:
        shifted_str = num_str[-shift:] + num_str[:-shift]
        return shifted_str
