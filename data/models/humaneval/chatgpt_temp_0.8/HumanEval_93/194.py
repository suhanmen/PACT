def encode(message):
    encoded_message = ''
    vowels = 'aeiou'
    for letter in message:
        # Swap case of all letters
        if letter.isupper():
            encoded_message += letter.lower()
        elif letter.islower():
            encoded_message += letter.upper()
        else:
            encoded_message += letter
        # Replace all vowels in the message with the letter
        # that appears 2 places ahead of that vowel in the english alphabet
        if letter.lower() in vowels:
            new_letter = chr(ord(letter) + 2)
            if new_letter in vowels:
                new_letter = chr(ord(new_letter) + 2)
            encoded_message = encoded_message[:-1] + new_letter.upper()
    return encoded_message
