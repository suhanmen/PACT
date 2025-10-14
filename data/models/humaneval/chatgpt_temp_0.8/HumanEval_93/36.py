def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded += chr(ord(char) + 2)
            else:
                encoded += char.swapcase()
        else:
            encoded += char
    return encoded
