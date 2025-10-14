def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ''
    for c in message:
        if c.isalpha():
            if c.lower() in vowels:
                encoded += chr(ord(c) + 2)
            else:
                encoded += c.swapcase()
        else:
            encoded += c
    return encoded
