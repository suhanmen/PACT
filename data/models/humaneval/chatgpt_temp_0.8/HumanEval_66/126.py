def digitSum(s):
    """
    Task: Write a function that takes a string as input and returns the sum of the upper characters only ASCII codes.
    """
    sum = 0
    for ch in s:
        if ch.isupper():
            sum += ord(ch)
    return sum
