def solve(s):
    new_string = ""
    letters_count = 0
    for c in s:
        if c.isalpha():
            letters_count += 1
            new_string += c.lower() if c.isupper() else c.upper()
        else:
            new_string += c
    if letters_count == 0:
        new_string = new_string[::-1]
    return new_string
