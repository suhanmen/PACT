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
    
    # Iterate from a to b inclusive
    for i in range(a, b+1):
        # Convert i to a string so we can access individual digits
        str_i = str(i)
        # Iterate over each digit in str_i
        for digit in str_i:
            # Convert the digit back to an integer
            int_digit = int(digit)
            # If the digit is even and not already in the list, add it
            if int_digit % 2 == 0 and int_digit not in even_digits:
                even_digits.append(int_digit)
    
    # Sort the list of even digits in ascending order
    even_digits.sort()
    
    return even_digits
