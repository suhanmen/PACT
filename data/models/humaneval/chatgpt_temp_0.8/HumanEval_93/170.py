def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for letter in message:
        # swap case of letters
        if letter.isalpha():
            if letter.islower():
                letter = letter.upper()
            else:
                letter = letter.lower()
        
        # replace vowels with letter 2 places ahead in alphabet
        if letter.lower() in vowels:
            letter = chr(ord(letter) + 2)
            if letter.lower() in vowels:
                letter = chr(ord(letter) + 2)
        
        encoded_message += letter
    
    return encoded_message
