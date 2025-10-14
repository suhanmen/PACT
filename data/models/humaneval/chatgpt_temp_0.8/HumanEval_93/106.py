def encode(message):
    encoded_message = ""
    vowels = "aeiouAEIOU"
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_char = chr(ord(char) + 2)
            else:
                encoded_char = char
        
            if encoded_char.islower():
                encoded_message += encoded_char.upper()
            else:
                encoded_message += encoded_char.lower()
        else:
            encoded_message += char
    
    return encoded_message
