def digitSum(s):
    """
    Task: Write a function that takes a string as input and returns the sum of the upper characters only ASCII codes.
    """
    sum = 0
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            sum += ord(char)
    return sum
