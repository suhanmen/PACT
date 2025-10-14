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
    total = 0 # initialize a variable to keep track of the sum
    for char in s: # loop through each character in the string
        if char.isupper(): # check if the character is uppercase
            total += ord(char) # if it is, add its ASCII code to the sum
    return total # return the sum
