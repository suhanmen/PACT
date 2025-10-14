def solve(s):
    result = ""
    letters_count = 0
    
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
            letters_count += 1
        else:
            result += char
    
    if letters_count == 0:
        result = result[::-1]
    
    return result
