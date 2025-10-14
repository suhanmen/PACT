def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for letter in message:
        # Swap case of letter
        if letter.islower():
            letter = letter.upper()
        elif letter.isupper():
            letter = letter.lower()
            
        # Replace vowel with letter 2 places ahead
        if letter in vowels:
            letter_index = ord(letter.lower()) - 97
            encoded_letter_index = (letter_index + 2) % 26
            encoded_letter = chr(encoded_letter_index + 97)
            letter = encoded_letter.upper()
            
        encoded_message += letter
        
    return encoded_message
