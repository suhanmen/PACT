def digitSum(s):
    upper_sum = 0
    for letter in s:
        if letter.isupper():
            upper_sum += ord(letter)
    return upper_sum
