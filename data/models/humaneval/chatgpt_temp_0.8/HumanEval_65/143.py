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
    num_digits = len(str_x)
    if shift > num_digits:
        return str_x[::-1] # return the digits reversed
    else:
        shift %= num_digits # wrap around shift if greater than number of digits
        shifted_str = str_x[-shift:] + str_x[:-shift] # shift digits to the right
        return shifted_str
