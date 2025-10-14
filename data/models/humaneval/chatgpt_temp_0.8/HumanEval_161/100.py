def solve(s):
    letters = False
    new_s = ""
    for i in s:
        if i.isalpha():
            letters = True
            if i.islower():
                new_s += i.upper()
            else:
                new_s += i.lower()
        else:
            new_s += i
    if not letters:
        new_s = s[::-1]
    return new_s
