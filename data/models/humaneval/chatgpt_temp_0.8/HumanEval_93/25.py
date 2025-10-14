def encode(message):
    encoded_message = ''
    vowels = 'aeiouAEIOU'
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded_letter = chr(ord(letter)+2)
                if encoded_letter in vowels:
                    encoded_letter = chr(ord(encoded_letter)+2)
            else:
                encoded_letter = letter.swapcase()
            encoded_message += encoded_letter
        else:
            encoded_message += letter
    return encoded_message
