def circular_shift(x, shift):
    # Convert input x to a string for easier manipulation
    x_str = str(x)
    
    # Determine the length of the string
    length = len(x_str)
    
    # If shift is greater than length, reverse the string
    if shift > length:
        return x_str[::-1]
    
    # Perform the circular shift
    shifted_str = x_str[-shift:] + x_str[:-shift]
    
    # Return the shifted string
    return shifted_str
