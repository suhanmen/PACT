def generate_integers(a, b):
    # Swap a and b if a is greater than b
    if a > b:
        a, b = b, a
    
    # Initialize an empty list to store the even digits
    even_digits = []
    
    # Loop through the range from a to b (inclusive)
    for num in range(a, b+1):
        # Convert the number to a string so we can check each digit
        digits = str(num)
        
        # Loop through each digit in the string
        for digit in digits:
            # If the digit is even and not already in the even_digits list, add it
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))

    # Sort the even_digits list in ascending order
    even_digits.sort()

    # Return the list of even digits
    return even_digits
