def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer x to a string and get its length
    x_str = str(x)
    n = len(x_str)

    # If shift > n, reverse the digits
    if shift > n:
        return x_str[::-1]

    # Shift the digits right by shift
    shifted_str = x_str[n-shift:] + x_str[:n-shift]

    return shifted_str
