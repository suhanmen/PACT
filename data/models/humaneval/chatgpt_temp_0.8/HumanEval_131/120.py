def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    
    # Convert the integer to a string to access individual digits
    n_str = str(n)
    
    # Initialize product to 1
    product = 1
    
    # Iterate over each digit in the string
    for digit in n_str:
        
        # Convert the digit back to an integer
        digit_int = int(digit)
        
        # Check if the digit is odd
        if digit_int % 2 == 1:
            
            # If it is odd, multiply it to the product
            product *= digit_int
    
    # Check if the product is still 1 (i.e. no odd digits)
    if product == 1:
        return 0
    else:
        return product
