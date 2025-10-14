def solve(s):
    letter_count = 0
    result = ""
    for char in s:
        if char.isalpha():
            letter_count += 1
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if letter_count == 0:
        result = result[::-1]
    return result
