def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            char = chr(ord(char)+2)
        elif char.isalpha():
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
        result += char
    return result
