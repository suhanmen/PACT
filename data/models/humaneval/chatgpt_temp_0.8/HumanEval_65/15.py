def circular_shift(x, shift):
    digits = str(x)
    num_digits = len(digits)
    
    if shift > num_digits:
        return digits[::-1]
    else:
        shifted_digits = digits[-shift:] + digits[:-shift]
        return shifted_digits
