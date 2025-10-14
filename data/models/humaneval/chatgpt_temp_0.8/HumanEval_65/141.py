def circular_shift(x, shift):
    x_str = str(x)
    length = len(x_str)
    shift = shift % length
    if shift == 0:
        return x_str
    elif shift > length:
        return x_str[::-1]
    else:
        return x_str[length-shift:] + x_str[:length-shift]
