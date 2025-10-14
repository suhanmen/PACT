def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    shift = shift % num_digits # reduce shift to be within range of number of digits
    
    if shift == 0:
        return x_str
    elif shift > num_digits:
        return x_str[::-1]

    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str
