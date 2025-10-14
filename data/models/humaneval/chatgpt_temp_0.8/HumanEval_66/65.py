def digitSum(s):
    sum = 0
    for i in s:
        if i.isupper():
            sum += ord(i)
    return sum
