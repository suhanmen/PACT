def circular_shift(x, shift):
    # Convert integer to string to make it iterable
    x_str = str(x)
    
    # Handle case where shift is greater than number of digits
    if shift > len(x_str):
        return x_str[::-1] # Return digits reversed
    
    # Perform circular shift by slicing and concatenating strings
    shifted_str = x_str[-shift:] + x_str[:-shift]
    
    # Convert shifted string back to integer and then to string for return
    return str(int(shifted_str))
