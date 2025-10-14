def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Initialize the product to 1
    product = 1
    # Convert the integer to a string to iterate over its digits
    n_str = str(n)
    # Loop through each digit in the string
    for digit in n_str:
        # Convert the digit back to an integer
        digit_int = int(digit)
        # If the digit is odd, multiply it by the product
        if digit_int % 2 == 1:
            product *= digit_int
    # If all digits are even, set the product to 0
    if product == 1:
        product = 0
    return product
