def solve(s):
    result = ""
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    if not has_letter:
        result = s[::-1]
    return result
