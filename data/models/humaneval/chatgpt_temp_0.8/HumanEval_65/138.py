def circular_shift(x, shift):
    x_str = str(x)
    if shift > len(x_str):
        return x_str[::-1]
    else:
        shift = shift % len(x_str)
        return x_str[-shift:] + x_str[:-shift]
