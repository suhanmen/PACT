def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    
    if shift > num_digits:
        # If shift > number of digits, return digits reversed
        return x_str[::-1]
    else:
        # Circular shift the digits right by shift and return the result as a string
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str
