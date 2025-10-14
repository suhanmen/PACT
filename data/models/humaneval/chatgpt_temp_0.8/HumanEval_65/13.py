def circular_shift(x, shift):
    s = str(x)
    n = len(s)
    if shift > n:
        return s[::-1]
    else:
        return s[-shift:] + s[:-shift]
