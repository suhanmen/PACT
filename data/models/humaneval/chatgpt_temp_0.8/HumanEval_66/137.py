def digitSum(s):
    sum_upper = 0
    for c in s:
        if c.isupper():
            sum_upper += ord(c)
    return sum_upper
