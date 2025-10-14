def solve(s):
    result = ""
    has_letters = False
    for char in s:
        if char.isalpha():
            has_letters = True
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    if not has_letters:
        result = result[::-1]
    return result
