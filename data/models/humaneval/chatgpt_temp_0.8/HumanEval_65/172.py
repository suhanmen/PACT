def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    if shift > num_digits:
        return x_str[::-1]  # reverse the digits
    shift = shift % num_digits  # handle shift greater than num_digits
    return x_str[-shift:] + x_str[:-shift]
