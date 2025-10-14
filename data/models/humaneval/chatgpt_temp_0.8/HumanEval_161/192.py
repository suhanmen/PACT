def solve(s):
    letters = 0
    for i in range(len(s)):
        if s[i].isalpha():
            letters += 1
            if s[i].isupper():
                s = s[:i] + s[i].lower() + s[i+1:]
            else:
                s = s[:i] + s[i].upper() + s[i+1:]
    if letters == 0:
        s = s[::-1]
    return s
