def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += vowels[char.lower()]
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message
