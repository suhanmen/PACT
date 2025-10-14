def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for letter in message:
        if letter.lower() in vowels:
            encoded_message += chr(ord(letter) + 2)
        elif letter.islower():
            encoded_message += letter.upper()
        elif letter.isupper():
            encoded_message += letter.lower()
        else:
            encoded_message += letter
    return encoded_message
