def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                new_letter = chr(ord(letter) + 2)
            else:
                new_letter = letter.swapcase()
            encoded += new_letter
        else:
            encoded += letter
    return encoded
