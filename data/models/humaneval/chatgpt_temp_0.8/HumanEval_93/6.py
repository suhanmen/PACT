def encode(message):
    vowels = 'aeiouAEIOU'
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded += chr(ord(letter) + 2) # replace vowel with letter 2 places ahead
            else:
                if letter.isupper():
                    encoded += letter.lower() # swap case
                else:
                    encoded += letter.upper() # swap case  
        else:
            encoded += letter
    return encoded
