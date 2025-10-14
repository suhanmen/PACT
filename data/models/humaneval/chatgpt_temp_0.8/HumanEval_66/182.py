def digitSum(s):
    """
    Write a function that takes a string as input and returns the sum of the ASCII codes
    of the uppercase characters only.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # initialize the sum to 0
    sum = 0
    # loop through each character in the string
    for char in s:
        # check if the character is uppercase
        if char.isupper():
            # add the ASCII code of the character to the sum
            sum += ord(char)
    # return the sum
    return sum
