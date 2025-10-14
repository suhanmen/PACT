def encode(message):
    encoded = ''
    vowels = 'aeiou'
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded += chr(ord(char) + 2).upper()
            else:
                if char.isupper():
                    encoded += char.lower()
                else:
                    encoded += char.upper()
        else:
            encoded += char
    return encoded
