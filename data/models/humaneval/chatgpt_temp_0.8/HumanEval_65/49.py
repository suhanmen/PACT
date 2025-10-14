def circular_shift(x, shift):
    str_x = str(x)
    num_digits = len(str_x)
    if shift > num_digits:
        return str_x[::-1]
    else:
        shifted_str = str_x[-shift:] + str_x[:-shift]
        return shifted_str
