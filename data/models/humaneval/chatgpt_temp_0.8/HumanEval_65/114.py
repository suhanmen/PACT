def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    if shift > n:
        return x_str[::-1]
    else:
        shifted_str = x_str[n-shift:] + x_str[:n-shift]
        return shifted_str
