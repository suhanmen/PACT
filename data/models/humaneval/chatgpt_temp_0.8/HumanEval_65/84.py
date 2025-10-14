def circular_shift(x, shift):
    digits = str(x)
    num_digits = len(digits)
    if shift > num_digits:
        return digits[::-1]
    else:
        return digits[-shift:] + digits[:-shift]
