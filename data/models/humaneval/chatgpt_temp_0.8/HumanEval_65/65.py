def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    # handle case where shift is greater than number of digits
    if shift > n:
        return x_str[::-1]
    # shift the digits right
    shifted = x_str[-shift:] + x_str[:n-shift]
    return shifted
