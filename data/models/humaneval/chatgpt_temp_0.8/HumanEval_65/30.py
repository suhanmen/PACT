def circular_shift(x, shift):
    x_str = str(x)
    shift = shift % len(x_str)
    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str[::-1] if shift > len(x_str)//2 else shifted_str
