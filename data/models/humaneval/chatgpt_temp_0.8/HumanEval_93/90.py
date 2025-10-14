def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for letter in message:
        if letter.lower() in vowels:
            new_letter = chr(ord(letter) + 2)
            if ord(new_letter) > ord('z'):
                new_letter = chr(ord(new_letter) - 26)
            encoded_message += new_letter.upper()
        else:
            if letter.isupper():
                encoded_message += letter.lower()
            else:
                encoded_message += letter.upper()
    return encoded_message
