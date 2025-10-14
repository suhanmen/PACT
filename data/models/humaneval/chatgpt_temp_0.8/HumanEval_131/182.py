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
    
    # Loop through each digit of n
    while n > 0:
        digit = n % 10
        
        # If the digit is odd, multiply it by the product
        if digit % 2 == 1:
            product *= digit
        
        # Update n to remove the last digit
        n //= 10
    
    # If the product is still 1, all digits were even, so return 0
    if product == 1:
        return 0
    else:
        return product
