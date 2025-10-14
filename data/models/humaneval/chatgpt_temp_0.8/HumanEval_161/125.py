def solve(s):
    letters = False
    new_s = ""
    for char in s:
        if char.isalpha():
            letters = True
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char
    if not letters:
        new_s = new_s[::-1]
    return new_s
