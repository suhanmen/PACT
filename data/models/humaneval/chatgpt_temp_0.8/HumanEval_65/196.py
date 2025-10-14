def circular_shift(x, shift):
    # convert x to a string so we can manipulate its digits
    x_str = str(x)
    n = len(x_str)

    # if shift is greater than n, just reverse the digits
    if shift >= n:
        return x_str[::-1]

    # otherwise, rotate the digits and return the result
    rotated_str = x_str[-shift:] + x_str[:-shift]
    return rotated_str
