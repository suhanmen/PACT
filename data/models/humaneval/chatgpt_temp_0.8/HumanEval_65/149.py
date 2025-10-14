def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x_str = str(x)
    length = len(x_str)
    if shift % length == 0:
        return x_str
    else:
        shift %= length
        shifted_str = x_str[-shift:] + x_str[:-shift]
        if shift > length // 2:
            shifted_str = shifted_str[::-1]
        return shifted_str
