def circular_shift(x, shift):
    num_digits = len(str(x))
    if shift > num_digits:
        x = str(x)[::-1]
        shift = num_digits - shift % num_digits
    else:
        shift = num_digits - shift
    x = str(x).zfill(num_digits)
    return str(x[-shift:] + x[:-shift])
