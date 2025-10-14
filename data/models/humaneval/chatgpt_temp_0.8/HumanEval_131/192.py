def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Convert n to a string to iterate through its digits
    n_str = str(n)
    # Initialize product as 1
    product = 1
    # Iterate through each digit and check if it's odd
    for digit in n_str:
        if int(digit) % 2 != 0:
            product *= int(digit)
    # If product is still 1, it means all digits were even, so return 0
    if product == 1:
        return 0
    else:
        return product
