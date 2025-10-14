def solve(s):
    new_str = ""
    letters_count = 0
    
    for char in s:
        if char.isalpha():
            if char.islower():
                new_str += char.upper()
            else:
                new_str += char.lower()
            letters_count += 1
        else:
            new_str += char
    
    if letters_count == 0:
        return new_str[::-1]
    else:
        return new_str
