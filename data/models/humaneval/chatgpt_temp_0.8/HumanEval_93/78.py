def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for letter in message:
        # Swap case of letter
        if letter.islower():
            letter = letter.upper()
        elif letter.isupper():
            letter = letter.lower()
        # Replace vowel with letter 2 places ahead in alphabet
        if letter in vowels:
            letter = chr(ord(letter) + 2)
        encoded_message += letter
    return encoded_message
