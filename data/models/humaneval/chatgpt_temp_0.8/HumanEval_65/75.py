def circular_shift(x, shift):
    x = str(x)
    if shift > len(x):
        return x[::-1]
    else:
        shifted = x[-shift:] + x[:-shift]
        return shifted
