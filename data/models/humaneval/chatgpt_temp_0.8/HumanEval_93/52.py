def encode(message):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded_message += chr(ord(letter)+2)
            else:
                encoded_message += letter.swapcase()
        else:
            encoded_message += letter
    return encoded_message
