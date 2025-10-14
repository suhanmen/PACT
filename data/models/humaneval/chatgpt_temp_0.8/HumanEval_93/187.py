def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_char = chr(ord(char) + 2)
            else:
                if char.isupper():
                    encoded_char = char.lower()
                else:
                    encoded_char = char.upper()
        else:
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message
