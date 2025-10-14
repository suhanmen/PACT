def solve(s):
    has_letter = False
    result = ""
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if not has_letter:
        result = s[::-1]
    return result
