def circular_shift(x, shift):
    x_str = str(x)
    x_len = len(x_str)
    shift = shift % x_len
    if shift == 0:
        return x_str
    elif shift > x_len:
        return x_str[::-1]
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str
