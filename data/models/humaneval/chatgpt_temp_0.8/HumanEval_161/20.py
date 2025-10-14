def solve(s):
    letters = 0
    new_s = ""
    for char in s:
        if char.isalpha():
            letters += 1
            if char.isupper():
                new_s += char.lower()
            else:
                new_s += char.upper()
        else:
            new_s += char
    if letters == 0:
        new_s = new_s[::-1]
    return new_s
