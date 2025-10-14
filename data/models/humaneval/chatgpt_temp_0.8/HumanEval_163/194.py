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
    
    # Loop through each number between a and b (inclusive)
    for num in range(a, b+1):
        # Convert the number to a string so we can access its digits
        str_num = str(num)
        
        # Loop through each digit in the string
        for digit in str_num:
            # Convert the digit back to an integer
            int_digit = int(digit)
            
            # If the digit is even and not already in the even_digits list, add it
            if int_digit % 2 == 0 and int_digit not in even_digits:
                even_digits.append(int_digit)
    
    # Sort the even_digits list in ascending order
    even_digits.sort()
    
    # Return the even_digits list
    return even_digits
