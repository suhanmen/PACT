def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    # Convert the integer n to a string to make it easier to handle the digits
    n_str = str(n)

    # Initialize the product variable to 1
    product = 1

    # Loop through each digit in the string
    for digit in n_str:
        # Convert the digit back to an integer
        digit_int = int(digit)
        # Check if the digit is odd
        if digit_int % 2 != 0:
            # Multiply the product by the odd digit
            product *= digit_int

    # If the product is still 1, that means there were no odd digits
    # so return 0
    if product == 1:
        return 0
    else:
        return product
