def encode(message):
    vowels = 'AEIOUaeiou'
    encoded = ''
    for letter in message:
        if letter in vowels:
            encoded += chr(ord(letter) + 2)
        else:
            encoded += letter.swapcase()
    return encoded
