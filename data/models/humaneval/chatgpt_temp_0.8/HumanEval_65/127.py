def circular_shift(x, shift):
    x_str = str(x) # Convert integer x to a string
    num_digits = len(x_str) # Find the number of digits in the string
    shift %= num_digits # Reduce the shift amount to be between 0 and num_digits
    if shift == 0:
        return x_str # No shift necessary, return original string
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift] # Perform circular shift
        if shift > num_digits // 2:
            shifted_str = shifted_str[::-1] # Reverse string if shift > num_digits/2
        return shifted_str
