def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                # encode the vowel
                encoded_char = chr(ord(char) + 2)
            else:
                # swap case of the letter
                if char.isupper():
                    encoded_char = char.lower()
                else:
                    encoded_char = char.upper()
        else:
            # non-alpha characters are not encoded
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message
