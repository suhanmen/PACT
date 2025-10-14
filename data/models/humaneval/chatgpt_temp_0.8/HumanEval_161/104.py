def solve(s):
    letters = 0
    for char in s:
        if char.isalpha():
            letters += 1
    if letters == 0:
        return s[::-1]
    else:
        return ''.join([char.lower() if char.isupper() else char.upper() if char.islower() else char for char in s])
