def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'AEIOUaeiou'
    encoded = ''
    for letter in message:
        if letter in vowels:
            new_letter = chr(ord(letter) + 2)
        else:
            new_letter = letter.swapcase()
        encoded += new_letter
    return encoded
