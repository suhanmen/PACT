def encode(message):
    vowels = 'AEIOUaeiou'
    encoded_message = ''
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
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message
