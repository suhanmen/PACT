def circular_shift(x, shift):
    # Convert integer to string for easier manipulation.
    x_str = str(x)
    # If shift is greater than number of digits, reverse digits.
    if shift >= len(x_str):
        return x_str[::-1]
    # Circularly shift digits to the right.
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str
