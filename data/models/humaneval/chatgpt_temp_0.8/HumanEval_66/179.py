def digitSum(s):
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total
