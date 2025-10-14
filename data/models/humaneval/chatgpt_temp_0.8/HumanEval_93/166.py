def encode(message):
    encoded_message = ""
    
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_message += letter.upper()
            else:
                encoded_message += letter.lower()
                
            if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                encoded_message += chr(ord(letter) + 2)
            else:
                encoded_message += letter
        else:
            encoded_message += letter
            
    return encoded_message
