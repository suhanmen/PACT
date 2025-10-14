def encode(message):
    encoded_message = ''
    vowels = 'AEIOUaeiou'
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_char = chr(ord(char)+2)
            else:
                encoded_char = char
            
            if encoded_char.isupper():
                encoded_char = encoded_char.lower()
            else:
                encoded_char = encoded_char.upper()
        else:
            encoded_char = char
            
        encoded_message += encoded_char
        
    return encoded_message
