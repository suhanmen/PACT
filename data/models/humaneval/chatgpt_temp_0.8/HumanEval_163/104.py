def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Initialize an empty list to store the even digits
    even_digits = []
    
    # If a is greater than b, swap them
    if a > b:
        a, b = b, a
    
    # Loop through the range of numbers between a and b (inclusive)
    for i in range(a, b+1):
        # Convert the number to a string to check its digits
        num_str = str(i)
        # Loop through the digits of the number
        for digit in num_str:
            # If the digit is even, append it to the list of even digits
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))
    
    # Return the list of even digits in ascending order
    return sorted(even_digits)
