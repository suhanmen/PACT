def solve(s):
    new_s = ""
    has_letters = False
    for char in s:
        if char.isalpha():
            has_letters = True
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char
    
    if not has_letters:
        new_s = new_s[::-1]
    
    return new_s
