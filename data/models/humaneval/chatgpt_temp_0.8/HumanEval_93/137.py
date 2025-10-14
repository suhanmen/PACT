def encode(message):
    vowels = 'aeiouAEIOU'
    encoded = ''
    for char in message:
        if char in vowels:
            encoded_char = chr(ord(char) + 2) # shift the vowel 2 places ahead
        elif char.isalpha():
            encoded_char = char.swapcase() # swap the case of the letter
        else:
            encoded_char = char
        encoded += encoded_char
    return encoded
