def encode(message):
    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded += chr(ord(char) + 2) # replace vowel with letter 2 places ahead in alphabet
            else:
                if char.islower():
                    encoded += char.upper() # swap case
                else:
                    encoded += char.lower()
        else:
            encoded += char
    return encoded
