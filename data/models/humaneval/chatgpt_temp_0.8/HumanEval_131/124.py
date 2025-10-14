def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Initialize product to 1
    product = 1
    # Convert integer to string for easy iteration
    for digit in str(n):
        # Check if digit is odd
        if int(digit) % 2 == 1:
            # Multiply to product
            product *= int(digit)
    # If product is still 1, then all digits are even
    if product == 1:
        return 0
    else:
        return product
