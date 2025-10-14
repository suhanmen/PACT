def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for letter in message:
        if letter.lower() in vowels:
            encoded_message += chr(ord(letter) + 2)
        else:
            encoded_message += letter.swapcase()
    return encoded_message
