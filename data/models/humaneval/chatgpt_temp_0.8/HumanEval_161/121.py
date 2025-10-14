def solve(s):
    result = ""
    contains_letters = False
    for char in s:
        if char.isalpha():
            result += char.swapcase()
            contains_letters = True
        else:
            result += char
    if not contains_letters:
        result = result[::-1]
    return result
