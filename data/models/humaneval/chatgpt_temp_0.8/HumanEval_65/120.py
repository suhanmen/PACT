def circular_shift(x, shift):
    x = str(x)
    n = len(x)
    if shift > n:
        return x[::-1]
    shift = shift % n
    return x[-shift:] + x[:n-shift]
