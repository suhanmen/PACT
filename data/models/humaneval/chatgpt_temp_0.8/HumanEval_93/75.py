def encode(message):
    vowels = "aeiouAEIOU"
    encoded_message = ""
    
    for char in message:
        # Swap case of all letters
        if char.isalpha():
            if char.isupper():
                encoded_message += char.lower()
            else:
                encoded_message += char.upper()
        else:
            encoded_message += char
        
        # Replace vowels with letter 2 places ahead in alphabet
        if char in vowels:
            encoded_message = encoded_message[:-1] + chr(ord(char) + 2)
    
    return encoded_message
