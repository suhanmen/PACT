def encode(message):
    vowels = "aeiou"
    encoded_message = ""
    for char in message:
        if char.lower() in vowels:
            new_char = chr(ord(char)+2)
        else:
            new_char = char.swapcase()
        encoded_message += new_char
    return encoded_message
