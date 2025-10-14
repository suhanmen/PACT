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
    
    # Convert the integer to a string to iterate over each digit
    for digit in str(n):
        # Convert the digit back to an integer
        digit = int(digit)
        # If the digit is odd, multiply it by the product
        if digit % 2 != 0:
            product *= digit
    
    # If the product is still 1, all digits were even, so return 0
    if product == 1:
        return 0
    else:
        return product
