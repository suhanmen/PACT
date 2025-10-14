def digitSum(s):
    upper_sum = 0
    for c in s:
        if c.isupper():
            upper_sum += ord(c)
    return upper_sum
