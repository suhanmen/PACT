def solve(s):
    new_s = ""
    contains_letter = False
    for char in s:
        if char.isalpha():
            contains_letter = True
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char
    if not contains_letter:
        return new_s[::-1]
    else:
        return new_s
