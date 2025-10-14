python
def encode(message):
    """
    Takes a message and encodes it by swapping case of all letters,
    and replacing all vowels in the message with the letter that appears
    2 places ahead of that vowel in the english alphabet. Assumes only letters.
    """
    vowels = 'aeiou'
    encoded_message = ''
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                # replace with letter 2 places ahead in alphabet
                encoded_message += chr(ord(char) + 2).swapcase()
            else:
                # swap case of non-vowel letters
                encoded_message += char.swapcase()
        else:
            # pass through non-letter characters
            encoded_message += char
            
    return encoded_message
