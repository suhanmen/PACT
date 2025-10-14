def digitSum(s):
    # Initialize the sum of ASCII codes to 0
    sum_ascii = 0

    # Iterate through each character in the string
    for c in s:
        # Check if the character is uppercase
        if c.isupper():
            # Add the ASCII code of the character to the sum
            sum_ascii += ord(c)

    # Return the sum of ASCII codes
    return sum_ascii
