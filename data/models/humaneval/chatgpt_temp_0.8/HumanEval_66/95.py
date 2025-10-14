def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Initialize sum to 0
    sum = 0
    
    # Iterate over each character in the string
    for c in s:
        # If the character is uppercase, add its ASCII code to the sum
        if c.isupper():
            sum += ord(c)
    
    # Return the sum
    return sum
