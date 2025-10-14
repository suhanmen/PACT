def solve(s):
    new_s = ""
    letters_exist = False
    
    for char in s:
        if char.isalpha():
            letters_exist = True
            if char.isupper():
                new_s += char.lower()
            else:
                new_s += char.upper()
        else:
            new_s += char
    
    if not letters_exist:
        new_s = s[::-1]
        
    return new_s
