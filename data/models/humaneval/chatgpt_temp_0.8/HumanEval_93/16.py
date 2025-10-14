def encode(message):
    vowels = 'aeiouAEIOU'
    encoded = ''
    for letter in message:
        # swap case of letter
        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
        # replace vowels
        if letter in vowels:
            encoded += chr(ord(letter) + 2)
        else:
            encoded += letter
    return encoded
