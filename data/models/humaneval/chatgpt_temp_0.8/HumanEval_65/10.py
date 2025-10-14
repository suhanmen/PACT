def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    shift = shift % n
    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        if shift > n // 2:
            return shifted_str[::-1]
        else:
            return shifted_str
