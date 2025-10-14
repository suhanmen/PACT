def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    shift = shift % num_digits
    if shift == 0:
        return x_str
    elif shift > num_digits // 2:
        return x_str[::-1]
    else:
        return x_str[-shift:] + x_str[:-shift]
