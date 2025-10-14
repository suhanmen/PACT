def encode(message):
    vowels = set('aeiouAEIOU')
    encoded = ''
    for letter in message:
        if letter in vowels:
            encoded += chr(ord(letter) + 2)
        elif letter.islower():
            encoded += letter.upper()
        else:
            encoded += letter.lower()
    return encoded
