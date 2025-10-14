def circular_shift(x, shift):
    str_x = str(x)
    n = len(str_x)
    if shift > n:
        return str_x[::-1]
    shift %= n
    return str_x[-shift:] + str_x[:-shift]
