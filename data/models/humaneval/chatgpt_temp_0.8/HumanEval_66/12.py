def digitSum(s):
    sum = 0   # initialize the sum to 0
    for c in s:   # loop through each character in the string
        if c.isupper():   # check if the character is uppercase
            sum += ord(c)   # add the ASCII code of the character to the sum
    return sum   # return the final sum
