def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    if shift > n:
        return x_str[::-1]  # Reverse the digits if shift > n
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]  # Perform circular shift
        return shifted_str
