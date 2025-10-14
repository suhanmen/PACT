def digitSum(s):
    total_sum = 0
    for char in s:
        if char.isupper():
            total_sum += ord(char)
    return total_sum
