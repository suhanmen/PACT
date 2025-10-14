def circular_shift(x, shift):
    # convert integer to string for easier manipulation
    x_str = str(x)
    
    # if shift is greater than number of digits, reverse the string
    if shift >= len(x_str):
        return x_str[::-1]
    
    # shift the digits to the right
    shifted_str = x_str[-shift:] + x_str[:-shift]
    
    return shifted_str
