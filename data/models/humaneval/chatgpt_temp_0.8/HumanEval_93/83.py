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
    vowels = 'aeiouAEIOU'
    encoded = ''
    for letter in message:
        if letter in vowels:
            encoded += chr(ord(letter) + 2)
        elif letter.islower():
            encoded += letter.upper()
        elif letter.isupper():
            encoded += letter.lower()
        else:
            encoded += letter
    return encoded
