def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    shift = shift % n
    if shift == 0:
        return x_str
    elif shift > n:
        return x_str[::-1]
    else:
        return x_str[-shift:] + x_str[:-shift]
