def circular_shift(x, shift):
    # Convert the integer x to a string
    x_str = str(x)

    # Calculate the number of digits in x
    num_digits = len(x_str)

    # If shift > number of digits, return digits reversed
    if shift > num_digits:
        return x_str[::-1]

    # Perform circular shift by shifting the digits right by shift
    shifted_str = x_str[-shift:] + x_str[:-shift]

    # Return the result as a string
    return shifted_str
