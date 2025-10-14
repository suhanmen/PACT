def circular_shift(x, shift):
    x_str = str(x)
    shift = shift % len(x_str)  # Ensure shift is within range
    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]  # Circular shift
        return shifted_str[::-1]  # Reverse if shift > number of digits
