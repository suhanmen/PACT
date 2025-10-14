def digitSum(s):
    sum = 0
    for char in s:
        if char.isupper(): # check if the character is upper case
            sum += ord(char) # add the ASCII value of the character to the sum
    return sum
