def circular_shift(x, shift):
    x = str(x)
    length = len(x)
    shift = shift % length
    if shift == 0:
        return x
    elif shift > length:
        return x[::-1]
    else:
        return x[-shift:] + x[:length-shift]
