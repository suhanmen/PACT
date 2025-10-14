def circular_shift(x, shift):
    num_digits = len(str(x))
    shift = shift % num_digits
    if shift == 0:
        return str(x)
    elif shift > num_digits // 2:
        return str(x)[::-1]
    else:
        return str(x)[-shift:] + str(x)[:-shift]
