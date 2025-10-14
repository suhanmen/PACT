def solve(s):
    new_s = ""
    letters = 0
    for i in s:
        if i.isalpha():
            letters += 1
            if i.isupper():
                new_s += i.lower()
            else:
                new_s += i.upper()
        else:
            new_s += i
    if letters == 0:
        new_s = new_s[::-1]
    return new_s
