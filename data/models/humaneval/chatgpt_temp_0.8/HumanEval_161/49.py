def solve(s):
    letters = 0
    for char in s:
        if char.isalpha():
            letters += 1
    if letters == 0:
        return s[::-1]
    else:
        result = ""
        for char in s:
            if char.isalpha():
                if char.islower():
                    result += char.upper()
                else:
                    result += char.lower()
            else:
                result += char
        return result
