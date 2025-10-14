def circular_shift(x, shift):
    x_str = str(x)
    n = len(x_str)
    if shift > n:
        return x_str[::-1] # Return digits reversed
    else:
        return x_str[-shift:] + x_str[:-shift] # Circular shift by shift digits to the right
