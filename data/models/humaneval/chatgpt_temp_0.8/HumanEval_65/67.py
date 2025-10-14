def circular_shift(x, shift):
    # convert x to string for easier manipulation
    x_str = str(x)
    # calculate the total number of digits in x
    num_digits = len(x_str)
    # calculate the effective shift amount
    shift %= num_digits
    # if shift is zero, return x_str as is
    if shift == 0:
        return x_str
    # if shift is greater than num_digits, reverse x_str and return it
    if shift > num_digits:
        return x_str[::-1]
    # otherwise, perform the circular shift
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str
