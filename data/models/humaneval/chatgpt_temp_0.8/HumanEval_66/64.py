def digitSum(s):
    total = 0
    for c in s:
        if c.isupper():
            total += ord(c)
    return total
