def digitSum(s):
    sum_upper = 0
    for letter in s:
        if letter.isupper():
            sum_upper += ord(letter)
    return sum_upper
