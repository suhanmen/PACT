def encode(message):
    """
    Encode message by swapping case of all letters, replacing all vowels in 
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
        if letter.isalpha():
            # swap case
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
                
            # replace vowels
            if letter in vowels:
                index = ord(letter) + 2
                if letter.isupper() and index > ord('Z'):
                    index -= 26
                elif letter.islower() and index > ord('z'):
                    index -= 26
                letter = chr(index)
        
        encoded += letter
    
    return encoded
