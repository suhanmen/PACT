def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x_str = str(x)
    length = len(x_str)
    if shift > length:
        return x_str[::-1]
    else:
        return x_str[length-shift:] + x_str[:length-shift]
