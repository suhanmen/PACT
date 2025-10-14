def solve(s):
    letters = 0
    for char in s:
        if char.isalpha():
            letters += 1
    
    if letters == 0:
        return s[::-1]
    
    result = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                result.append(char.lower())
            else:
                result.append(char.upper())
        else:
            result.append(char)
    
    return "".join(result)
