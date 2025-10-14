def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    shift = shift % num_digits
    if shift == 0:
        return x_str
    if shift > num_digits:
        return x_str[::-1]
    return x_str[-shift:] + x_str[:-shift]
