def circular_shift(x, shift):
    x_str = str(x)
    length = len(x_str)
    if shift > length:
        return x_str[::-1]
    else:
        return x_str[length-shift:] + x_str[:length-shift]
