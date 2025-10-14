def digitSum(s):
    # Initialize the sum to 0
    sum = 0
    
    # Iterate over each character in the string
    for c in s:
        # Check if the character is uppercase
        if c.isupper():
            # Add the ASCII code of the character to the sum
            sum += ord(c)
    
    # Return the sum
    return sum
