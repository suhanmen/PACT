def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create an empty list to store the even digits
    even_digits = []
    
    # Loop through all the numbers between a and b
    for num in range(min(a, b), max(a, b)+1):
        # Check if the number is even and has more than one digit
        if num % 2 == 0 and len(str(num)) > 1:
            # Loop through each digit in the number
            for digit in str(num):
                # Check if the digit is even and add it to the list if it is
                if int(digit) % 2 == 0:
                    even_digits.append(int(digit))
    
    # Sort the list in ascending order and return it
    return sorted(even_digits)
