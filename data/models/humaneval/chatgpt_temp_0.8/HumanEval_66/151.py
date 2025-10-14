def digitSum(s):
    upper_sum = 0
    for char in s:
        if char.isupper():
            upper_sum += ord(char)
    return upper_sum
