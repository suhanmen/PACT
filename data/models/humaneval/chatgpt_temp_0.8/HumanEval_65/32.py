def circular_shift(x, shift):
    # Convert x to a string to easily manipulate its individual digits
    x_str = str(x)
    num_digits = len(x_str)

    # If shift is greater than the number of digits, reverse the digits of x
    if shift >= num_digits:
        return x_str[::-1]

    # Shift the digits to the right by shift
    shifted_str = x_str[-shift:] + x_str[:-shift]

    return shifted_str
