def solve(s):
    is_letter = False
    for char in s:
        if char.isalpha():
            is_letter = True
            break
    
    if not is_letter:
        return s[::-1]
    
    result = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    
    return result
