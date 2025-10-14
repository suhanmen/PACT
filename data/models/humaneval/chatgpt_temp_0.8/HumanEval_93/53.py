def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                encoded_message += vowels[letter.lower()]
            else:
                if letter.islower():
                    encoded_message += letter.upper()
                else:
                    encoded_message += letter.lower()
        else:
            encoded_message += letter
    return encoded_message
