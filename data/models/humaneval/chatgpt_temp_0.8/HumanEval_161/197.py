def solve(s):
    is_letter_present = False
    new_s = ""
    
    for char in s:
        if char.isalpha():
            is_letter_present = True
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char
    
    if not is_letter_present:
        new_s = s[::-1]
        
    return new_s
