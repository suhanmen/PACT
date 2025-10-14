def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                encoded_message += chr(ord(letter) + 2)
            else:
                if letter.isupper():
                    encoded_message += letter.lower()
                else:
                    encoded_message += letter.upper()
        else:
            encoded_message += letter
    return encoded_message
