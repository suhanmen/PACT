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
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            # Swap the case of the letter
            if letter.islower():
                encoded_letter = letter.upper()
            else:
                encoded_letter = letter.lower()
            # Replace vowels with the letter 2 places ahead in the alphabet
            if encoded_letter in 'AEIOU':
                encoded_letter = chr(ord(encoded_letter) + 2)
                if encoded_letter > 'Z':
                    encoded_letter = chr(ord(encoded_letter) - 26)
        else:
            encoded_letter = letter
        encoded_message += encoded_letter
    return encoded_message
