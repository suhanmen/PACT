def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ''
    for char in message:
        if char.lower() in vowels:
            encoded += chr(ord(char.lower()) + 2).upper()
        elif char.islower():
            encoded += char.upper()
        elif char.isupper():
            encoded += char.lower()
        else:
            encoded += char
    return encoded
