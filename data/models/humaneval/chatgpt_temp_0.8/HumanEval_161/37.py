def solve(s):
    res = ""
    letters = False
    
    for char in s:
        if char.isalpha():
            letters = True
            if char.isupper():
                res += char.lower()
            else:
                res += char.upper()
        else:
            res += char
    
    if not letters:
        res = s[::-1]
    
    return res
