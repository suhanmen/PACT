def solve(s):
    new_str = ""
    has_letters = False
    for char in s:
        if char.isalpha():
            has_letters = True
            if char.isupper():
                new_str += char.lower()
            else:
                new_str += char.upper()
        else:
            new_str += char
    if not has_letters:
        new_str = new_str[::-1]
    return new_str
