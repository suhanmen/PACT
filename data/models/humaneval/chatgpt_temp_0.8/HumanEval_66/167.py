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

    # First, we need to filter out all non-upper characters
    upper_chars = [c for c in s if c.isupper()]

    # Then, we need to convert the characters to ASCII codes and sum them up
    return sum([ord(c) for c in upper_chars])
