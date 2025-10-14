def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    if shift > n:
        return x_str[::-1]
    else:
        shifted_x_str = x_str[-shift:] + x_str[:-shift]
        return shifted_x_str
