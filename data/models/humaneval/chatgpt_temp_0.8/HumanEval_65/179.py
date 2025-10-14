def circular_shift(x, shift):
    # Convert x to a string to access the individual digits
    x_str = str(x)
    # Find the number of digits in x
    num_digits = len(x_str)
    # If shift is greater than the number of digits, reverse the digits
    if shift > num_digits:
        return x_str[::-1]
    # Otherwise, shift the digits to the right
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str
