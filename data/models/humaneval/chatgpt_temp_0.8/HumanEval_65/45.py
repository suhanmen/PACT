def circular_shift(x, shift):
    # Convert x to a string for easy manipulation
    x_str = str(x)

    # If shift is greater than the number of digits, reverse the digits
    if shift >= len(x_str):
        return x_str[::-1]

    # Shift the digits to the right by shift
    shifted_str = x_str[-shift:] + x_str[:-shift]

    return shifted_str
