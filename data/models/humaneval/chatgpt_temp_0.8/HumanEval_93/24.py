def encode(message):
    """
    Encode a message by swapping case of all letters and replacing 
    vowels with the letter 2 places ahead in the English alphabet.
    """
    vowels = 'AEIOUaeiou'
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded += chr(ord(letter) + 2)
            else:
                encoded += letter.swapcase()
        else:
            encoded += letter
    return encoded
