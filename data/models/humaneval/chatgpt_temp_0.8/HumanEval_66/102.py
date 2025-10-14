def digitSum(s):
    # Initialize the sum to zero
    total = 0

    # Iterate over the characters in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the uppercase character to the total
            total += ord(char)

    # Return the total sum
    return total
