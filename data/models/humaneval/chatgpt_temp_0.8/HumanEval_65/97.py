def circular_shift(x, shift):
    x = str(x)  # convert integer to string for easier manipulation
    n = len(x)
    if shift == 0 or n == 1:  # no shift needed, or only one digit to shift
        return x
    elif shift > n:  # shift more than number of digits, return digits reversed
        return x[::-1]
    else:  # perform circular shift
        shift %= n
        return x[-shift:] + x[:-shift]
