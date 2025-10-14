def solve(s):
    letters = 0
    for char in s:
        if char.isalpha():
            letters += 1
    if letters == 0:
        return s[::-1]
    else:
        new_str = ""
        for char in s:
            if char.isalpha():
                if char.islower():
                    new_str += char.upper()
                else:
                    new_str += char.lower()
            else:
                new_str += char
        return new_str
