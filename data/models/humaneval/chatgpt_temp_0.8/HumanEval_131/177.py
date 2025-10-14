def digits(n):
    # Initialize product to 1
    product = 1
    # Convert n to string to iterate over digits
    n_str = str(n)
    # Iterate over digits
    for digit in n_str:
        # Convert digit to int
        digit_int = int(digit)
        # If digit is even, return 0
        if digit_int % 2 == 0:
            return 0
        # If digit is odd, multiply it with the product
        product *= digit_int
    # Return the final product
    return product
