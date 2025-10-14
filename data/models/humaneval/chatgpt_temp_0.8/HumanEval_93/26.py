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
    vowels = "aeiouAEIOU"
    encoded = ""
    
    for char in message:
        if char in vowels:
            if char == "u":
                encoded += "W"
            elif char == "U":
                encoded += "w"
            else:
                encoded += chr(ord(char) + 2)
        elif char.islower():
            encoded += char.upper()
        elif char.isupper():
            encoded += char.lower()
        else:
            encoded += char
            
    return encoded
