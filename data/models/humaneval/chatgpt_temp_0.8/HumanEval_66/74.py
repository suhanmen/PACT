def digitSum(s):
    """
    Task: Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Args:
    s: string

    Returns:
    int: sum of ASCII codes of uppercase characters

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)  # ord() returns the ASCII value of a character
    return sum
