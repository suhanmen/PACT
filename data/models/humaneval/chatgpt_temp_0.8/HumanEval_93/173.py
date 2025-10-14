def encode(message):
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                encoded_message += chr(ord(char)+2)
            else:
                encoded_message += char
        else:
            encoded_message += char
    return encoded_message
