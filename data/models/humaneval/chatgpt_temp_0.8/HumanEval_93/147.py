def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            # Swap case of letter
            if char.isupper():
                encoded_char = char.lower()
            else:
                encoded_char = char.upper()
            # Replace vowel with letter 2 places ahead
            if char in vowels:
                encoded_char = chr(ord(char) + 2)
                if encoded_char in vowels:
                    encoded_char = chr(ord(encoded_char) + 2)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message
