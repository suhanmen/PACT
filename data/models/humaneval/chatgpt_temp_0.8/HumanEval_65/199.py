def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    shift = shift % num_digits  # shift cannot be greater than num_digits
    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        if shift > num_digits / 2:
            return shifted_str[::-1]  # reverse the string if shift is greater than half of the digits
        else:
            return shifted_str
