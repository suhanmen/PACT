def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                encoded_message += chr(ord(letter) + 2)
            else:
                encoded_message += letter.swapcase()
        else:
            encoded_message += letter
    return encoded_message
