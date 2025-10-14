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

    # Loop through each digit of the integer
    for digit in str(n):
        # Convert the digit back to an integer
        digit = int(digit)
        # Check if the digit is odd
        if digit % 2 == 1:
            # Multiply the product by the odd digit
            product *= digit

    # If the product is still 1, then all digits are even
    if product == 1:
        return 0
    else:
        return product
