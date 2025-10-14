def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_char = chr(ord(char) + 2)
                if new_char in vowels:
                    new_char = chr(ord(new_char) + 2)
            else:
                new_char = char.swapcase()
            encoded_message += new_char
        else:
            encoded_message += char
    return encoded_message
