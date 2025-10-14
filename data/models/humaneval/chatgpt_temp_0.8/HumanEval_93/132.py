def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        # Swap the case of the letter
        if char.isupper():
            encoded_message += char.lower()
        elif char.islower():
            encoded_message += char.upper()
        else:
            encoded_message += char
        
        # Replace the vowel with a letter 2 places ahead in the alphabet
        if char in vowels:
            new_char = chr(ord(char) + 2)
            if new_char in vowels:
                new_char = chr(ord(new_char) + 2)
            encoded_message = encoded_message[:-1] + new_char
    
    return encoded_message
