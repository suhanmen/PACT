def solve(s):
    new_str = ""
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                new_str += char.upper()
            else:
                new_str += char.lower()
        else:
            new_str += char

    if not has_letter:
        new_str = new_str[::-1]

    return new_str
