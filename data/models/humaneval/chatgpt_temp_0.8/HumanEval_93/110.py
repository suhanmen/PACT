def encode(message):
    vowels = 'AEIOUaeiou'
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            encoded_letter = chr(ord(letter) + 2)
            encoded_message += encoded_letter
        elif letter.isupper():
            encoded_letter = letter.lower()
            encoded_message += encoded_letter
        elif letter.islower():
            encoded_letter = letter.upper()
            encoded_message += encoded_letter
        else:
            encoded_message += letter
    return encoded_message
