def solve(s):
    letters_found = False
    new_s = ""
    for char in s:
        if char.isalpha():
            letters_found = True
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char
    if not letters_found:
        new_s = s[::-1]
    return new_s
