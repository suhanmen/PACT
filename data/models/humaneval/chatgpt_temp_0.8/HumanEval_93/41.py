def encode(message):
    encoded_message = ''
    vowels = 'AEIOUaeiou'
    for char in message:
        # Swap case of letter
        if char.isalpha():
            if char.isupper():
                encoded_char = char.lower()
            else:
                encoded_char = char.upper()
            # Replace vowel with letter 2 places ahead in alphabet
            if encoded_char in vowels:
                encoded_char = chr(ord(encoded_char) + 2)
                if encoded_char > 'Z' and encoded_char < 'a':
                    encoded_char = chr(ord(encoded_char) - 26)
                elif encoded_char > 'z':
                    encoded_char = chr(ord(encoded_char) - 26)
        else:
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message
