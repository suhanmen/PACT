def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    encoded_message = ''
    for c in message:
        if c.isalpha():
            if c.lower() in vowels:
                encoded_message += vowels[c.lower()]
            else:
                encoded_message += c.swapcase()
        else:
            encoded_message += c
    return encoded_message
