def encode(message):
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            # Swap case of the letter
            if letter.isupper():
                encoded_letter = letter.lower()
            else:
                encoded_letter = letter.upper()
                
            # Replace vowels with letter 2 places ahead
            if encoded_letter in 'aeiou':
                encoded_letter = chr(ord(encoded_letter) + 2)
                if encoded_letter > 'z':
                    encoded_letter = chr(ord(encoded_letter) - 26)
            
            encoded_message += encoded_letter
        else:
            encoded_message += letter
    
    return encoded_message
