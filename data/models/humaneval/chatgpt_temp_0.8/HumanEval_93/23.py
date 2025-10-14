def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            new_char = chr(ord(char) + 2)
        elif char.isalpha():
            if char.islower():
                new_char = char.upper()
            else:
                new_char = char.lower()
        else:
            new_char = char
        
        result += new_char
    
    return result
