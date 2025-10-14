def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = str(x)
    num_digits = len(digits)
    shift = shift % num_digits  # to handle shift > num_digits case
    if shift == 0:
        return digits
    else:
        shifted_digits = digits[-shift:] + digits[:-shift]
        if shift > num_digits:
            return shifted_digits[::-1]  # reverse string if shift > num_digits
        else:
            return shifted_digits
