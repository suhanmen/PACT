def solve(s):
    letter_flag = False
    result = ''
    for char in s:
        if char.isalpha():
            result += char.swapcase()
            letter_flag = True
        else:
            result += char
    if not letter_flag:
        result = result[::-1]
    return result
