def solve(s):
    letters = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                letters.append(char.lower())
            else:
                letters.append(char.upper())
        else:
            letters.append(char)
    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return ''.join(letters)
