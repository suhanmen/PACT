def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            # Swap case of letter
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
            # Replace vowels with letter 2 places ahead in alphabet
            if letter in vowels:
                letter = chr(ord(letter) + 2)
                if letter > 'z':
                    letter = chr(ord(letter) - 26)
            encoded_message += letter
        else:
            encoded_message += letter
    return encoded_message
