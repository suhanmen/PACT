def generate_integers(a, b):
    # Swap the values of a and b if a is greater than b
    if a > b:
        a, b = b, a

    # Initialize an empty list to store the even digits
    even_digits = []

    # Loop through the range from a to b (inclusive)
    for i in range(a, b+1):
        # Convert the current number to a string
        str_i = str(i)

        # Loop through the digits of the current number
        for digit in str_i:
            # If the digit is even and not already in the list, add it
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))

    # Sort the even digits in ascending order
    even_digits.sort()

    # Return the list of even digits
    return even_digits
