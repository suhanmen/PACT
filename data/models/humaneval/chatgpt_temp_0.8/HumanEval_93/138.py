def encode(message):
    encoded_message = ""
    vowels = "aeiouAEIOU"
    for letter in message:
        if letter.isalpha():
            # swap case of letter
            if letter.isupper():
                encoded_letter = letter.lower()
            else:
                encoded_letter = letter.upper()
            
            # replace vowel with letter 2 places ahead
            if encoded_letter in vowels:
                encoded_letter = chr(ord(encoded_letter) + 2)
                if encoded_letter > 'Z' and encoded_letter < 'a':
                    encoded_letter = chr(ord(encoded_letter) - 26)

            encoded_message += encoded_letter
        else:
            encoded_message += letter
    
    return encoded_message
