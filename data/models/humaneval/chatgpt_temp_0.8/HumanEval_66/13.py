def digitSum(s):
    # Initialize sum variable to 0
    sum = 0
    # Loop through each character in the string
    for c in s:
        # If the character is uppercase, add its ASCII code to the sum
        if c.isupper():
            sum += ord(c)
    # Return the final sum
    return sum
