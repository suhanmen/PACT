def circular_shift(x, shift):
    x_string = str(x)
    length = len(x_string)
    shift = shift % length
    if shift == 0:
        return x_string
    elif shift > length:
        return x_string[::-1]
    else:
        return x_string[-shift:] + x_string[:-shift]
