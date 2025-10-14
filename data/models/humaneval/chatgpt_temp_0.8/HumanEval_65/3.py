def circular_shift(x, shift):
    x = str(x) # convert integer to string
    n = len(x)
    shift = shift % n # to handle shift greater than number of digits
    if shift == 0:
        return x
    elif shift > n:
        return x[::-1] # reverse the digits
    else:
        return x[-shift:] + x[:-shift]
