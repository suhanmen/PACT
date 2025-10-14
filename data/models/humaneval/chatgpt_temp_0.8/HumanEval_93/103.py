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
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for letter in message:
        if letter.lower() in vowels:
            encoded_message += chr(ord(letter) + 2)
        elif letter.islower():
            encoded_message += letter.upper()
        elif letter.isupper():
            encoded_message += letter.lower()
        else:
            encoded_message += letter
    return encoded_message
