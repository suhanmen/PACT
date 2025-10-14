def circular_shift(x, shift):
    x = str(x)
    n = len(x)
    shift = shift % n
    if shift == 0:
        return x
    elif shift > n:
        return x[::-1]
    else:
        return x[n-shift:] + x[:n-shift]
