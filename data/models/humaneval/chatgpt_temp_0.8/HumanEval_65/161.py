def circular_shift(x, shift):
    x_str = str(x)
    x_len = len(x_str)
    if shift > x_len:
        return x_str[::-1]
    else:
        return x_str[-shift:] + x_str[:-shift]
