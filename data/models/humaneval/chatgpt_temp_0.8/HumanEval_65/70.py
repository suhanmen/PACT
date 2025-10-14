def circular_shift(x, shift):
    # Convert x to a string to make it iterable
    x_str = str(x)
    # If shift > number of digits, return digits reversed
    if shift >= len(x_str):
        return x_str[::-1]
    # Circular shift the digits right by shift
    shifted_str = x_str[-shift:] + x_str[:-shift]
    # Return the shifted result as a string
    return shifted_str
