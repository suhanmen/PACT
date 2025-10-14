def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                # Replace vowel with letter 2 places ahead in alphabet
                encoded_message += chr(ord(letter) + 2)
            else:
                # Swap case of letter and add to encoded message
                encoded_message += letter.swapcase()
        else:
            # Add non-alpha character to encoded message
            encoded_message += letter
    return encoded_message
