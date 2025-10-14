def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    shift = shift % num_digits  # to handle cases where shift is greater than num_digits
    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        if shift > num_digits:
            shifted_str = x_str[::-1]
        return shifted_str
