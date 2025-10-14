def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Convert a and b to strings so we can iterate over their digits
    a_str, b_str = str(a), str(b)
    
    # Initialize an empty list to store the even digits
    even_digits = []
    
    # Iterate over the digits in a and b
    for digit in a_str + b_str:
        # Check if the digit is even and not already in the list
        if digit.isdigit() and int(digit) % 2 == 0 and int(digit) not in even_digits:
            # Add the even digit to the list
            even_digits.append(int(digit))
    
    # Sort the even digits in ascending order
    even_digits.sort()
    
    # Return the list of even digits
    return even_digits
