def circular_shift(x, shift):
    x_str = str(x)
    digits = len(x_str)
    shift = shift % digits
    if shift == 0:
        return x_str
    elif shift > digits:
        return x_str[::-1]
    else:
        return x_str[-shift:] + x_str[:-shift]
