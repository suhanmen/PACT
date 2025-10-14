def circular_shift(x, shift):
    # Convert the integer to a string to obtain its digits
    digits = str(x)
    
    # If shift is larger than the number of digits, reverse the digits
    if shift >= len(digits):
        return digits[::-1]
    
    # Shift the digits to the right
    shifted_digits = digits[-shift:] + digits[:-shift]
    
    # Return the shifted digits as a string
    return shifted_digits
