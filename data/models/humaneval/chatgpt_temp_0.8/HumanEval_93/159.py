def encode(message):
    encoded_message = ""
    vowels = "aeiouAEIOU"
    for char in message:
        if char.isalpha():
            # swap case of the letter
            if char.isupper():
                encoded_char = char.lower()
            else:
                encoded_char = char.upper()
            # replace vowels with letter 2 places ahead
            if encoded_char in vowels:
                encoded_char = chr(ord(encoded_char) + 2)
                if encoded_char in vowels:
                    encoded_char = chr(ord(encoded_char) + 2)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message
