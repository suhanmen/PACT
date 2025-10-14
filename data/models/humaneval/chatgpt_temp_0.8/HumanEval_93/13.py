def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                new_letter = chr(ord(letter) + 2)
            else:
                new_letter = letter.swapcase()
        else:
            new_letter = letter
        encoded_message += new_letter

    return encoded_message
