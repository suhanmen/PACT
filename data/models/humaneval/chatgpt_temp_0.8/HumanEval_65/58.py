def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert x to a string and get its length
    str_x = str(x)
    len_x = len(str_x)
    
    # If shift is greater than len_x, reverse the string and return it
    if shift >= len_x:
        return str_x[::-1]
    
    # Shift the string to the right by shift
    shifted_str = str_x[-shift:] + str_x[:-shift]
    
    return shifted_str
