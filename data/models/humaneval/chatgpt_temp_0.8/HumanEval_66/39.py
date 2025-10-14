def digitSum(s):
    """
    Task:
    Write a function that takes a string as input and returns the sum of the ASCII codes
    of the upper case characters in the string.

    Examples:
    digitSum("") => 0
    digitSum("abAB") => 131
    digitSum("abcCd") => 67
    digitSum("helloE") => 69
    digitSum("woArBld") => 131
    digitSum("aAaaaXa") => 153
    """
    upper_sum = 0
    for c in s:
        if c.isupper():
            upper_sum += ord(c)
    return upper_sum
