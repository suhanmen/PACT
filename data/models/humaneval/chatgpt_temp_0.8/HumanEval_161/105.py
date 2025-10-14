def solve(s):
    letters = 0
    result = ""
    for char in s:
        if char.isalpha():
            letters += 1
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if letters == 0:
        result = result[::-1]
    return result
