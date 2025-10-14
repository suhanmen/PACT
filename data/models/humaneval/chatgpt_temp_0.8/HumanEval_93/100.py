def encode(message):
    encoded = ''
    vowels = 'aeiouAEIOU'
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded += chr(ord(char)+2)
            else:
                encoded += char.swapcase()
        else:
            encoded += char
    return encoded
