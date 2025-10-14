def encode(message):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                new_char = chr(ord(char) + 2)
            else:
                new_char = char.swapcase()
            encoded_message += new_char
        else:
            encoded_message += char
    return encoded_message
