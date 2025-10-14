def circular_shift(x, shift):
    x = str(x)
    n = len(x)
    if shift > n:
        return x[::-1]
    else:
        return x[n-shift:] + x[:n-shift]
