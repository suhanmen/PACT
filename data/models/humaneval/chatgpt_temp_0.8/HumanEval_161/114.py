def solve(s):
    new_s = ""
    has_letter = False
    
    for c in s:
        if c.isalpha():
            has_letter = True
            if c.isupper():
                new_s += c.lower()
            else:
                new_s += c.upper()
        else:
            new_s += c
            
    if not has_letter:
        new_s = new_s[::-1]
        
    return new_s
