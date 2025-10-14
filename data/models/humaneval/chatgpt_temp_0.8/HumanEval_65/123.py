def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    if shift <= num_digits:
        shifted_str = x_str[-shift:] + x_str[:-shift]
    else:
        shifted_str = x_str[::-1]
    return shifted_str
