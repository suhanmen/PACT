def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    shift = shift % n  # Ensure that shift is within range of the number of digits
    if shift == 0:
        return x_str
    elif shift > n:
        return x_str[::-1]  # Reverse the string if shift is greater than the number of digits
    else:
        return x_str[-shift:] + x_str[:-shift]
