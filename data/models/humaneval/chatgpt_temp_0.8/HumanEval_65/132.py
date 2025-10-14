def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert integer to string for easier manipulation
    x_str = str(x)
    
    # Calculate the actual shift amount by taking the modulus of the shift with the length of the string
    actual_shift = shift % len(x_str)
    
    # If shift is greater than the length of the string, reverse the string
    if actual_shift == 0:
        return x_str[::-1]
    
    # Otherwise, perform the circular shift by concatenating the shifted and unshifted parts of the string
    return x_str[-actual_shift:] + x_str[:-actual_shift]
