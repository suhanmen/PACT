def circular_shift(x, shift):
    s = str(x)
    n = len(s)
    shift %= n  # limit shift to number of digits
    if shift == 0:  # no shift, return original string
        return s
    elif shift == n:  # shift by n is same as no shift, return string reversed
        return s[::-1]
    else:
        return s[-shift:] + s[:-shift]
