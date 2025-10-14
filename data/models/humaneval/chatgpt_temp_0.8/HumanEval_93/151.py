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

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    encoded = ''
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                # replace the vowel with the letter 2 places ahead in the alphabet
                encoded += chr(ord(char) + 2)
            else:
                # swap the case of the letter
                if char.isupper():
                    encoded += char.lower()
                else:
                    encoded += char.upper()
        else:
            # non-letter characters are unchanged
            encoded += char
            
    return encoded
