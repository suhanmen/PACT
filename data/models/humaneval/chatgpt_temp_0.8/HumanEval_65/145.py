def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert x to a string to get its length and to perform string operations
    x_str = str(x)
    n = len(x_str)
    
    # Calculate the actual shift value based on the length of x_str
    actual_shift = shift % n
    
    # If actual_shift is 0, then we don't need to shift at all
    if actual_shift == 0:
        return x_str
    
    # Otherwise, perform the circular shift
    shifted_str = x_str[-actual_shift:] + x_str[:-actual_shift]
    
    # If shift > number of digits, return digits reversed
    if shift > n:
        shifted_str = shifted_str[::-1]
    
    return shifted_str
