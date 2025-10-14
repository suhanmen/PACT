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
    encoded_message = ""
    vowels = "AEIOUaeiou"
    for char in message:
        if char.isalpha():
            # swap case of the letter
            if char.islower():
                encoded_char = char.upper()
            else:
                encoded_char = char.lower()
            
            # replace vowel with letter 2 places ahead of it
            if char in vowels:
                encoded_char = chr(ord(char) + 2)
                if encoded_char in vowels:
                    encoded_char = chr(ord(encoded_char) + 2)
            
            encoded_message += encoded_char
        else:
            encoded_message += char
            
    return encoded_message
