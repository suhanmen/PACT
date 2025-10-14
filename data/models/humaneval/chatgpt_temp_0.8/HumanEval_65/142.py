python
def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)

    if shift > num_digits:
        return x_str[::-1]

    new_str = x_str[-shift:] + x_str[:-shift]

    return new_str
