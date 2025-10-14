def solve(s):
    new_string = ''
    letter_count = 0
    
    for char in s:
        if char.isalpha():
            if char.isupper():
                new_string += char.lower()
            else:
                new_string += char.upper()
            letter_count += 1
        else:
            new_string += char
    
    if letter_count == 0:
        new_string = s[::-1]
    
    return new_string
