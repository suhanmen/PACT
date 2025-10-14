def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    if shift > num_digits:
        return x_str[::-1]  # Reversed string of digits
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]  # Shifted string of digits
        return shifted_str
