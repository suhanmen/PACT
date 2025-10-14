def circular_shift(x, shift):
    # Convert x to string for easy manipulation
    x_str = str(x)
    
    # Find number of digits in x
    num_digits = len(x_str)
    
    if shift > num_digits:
        # If shift is greater than number of digits,
        # reverse the digits and return as string
        return x_str[::-1]
    else:
        # Shift the digits to the right by shift positions
        shifted = x_str[-shift:] + x_str[:-shift]
        return shifted
