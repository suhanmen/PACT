def generate_integers(a, b):
    # Convert a and b to strings for easy iteration over the digits
    a_str = str(a)
    b_str = str(b)
    # Initialize an empty list to store the even digits
    even_digits = []
    # Loop over the digits in a and b
    for digit in range(len(a_str)):
        # Check if the digit is even
        if int(a_str[digit]) % 2 == 0:
            # Add it to the list of even digits
            even_digits.append(int(a_str[digit]))
    for digit in range(len(b_str)):
        if int(b_str[digit]) % 2 == 0:
            if int(b_str[digit]) not in even_digits:
                even_digits.append(int(b_str[digit]))
    # Sort the list in ascending order
    even_digits.sort()
    # Return the list of even digits
    return even_digits
