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
    new_message = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                new_letter = chr((ord(letter) + 2 - 65) % 26 + 65)
            else:
                new_letter = letter.swapcase()
            new_message += new_letter
        else:
            new_message += letter
    return new_message
