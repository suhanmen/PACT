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
    
    # Define a mapping of vowels to their 2-places-ahead letters
    vowel_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w',
    }
    
    # Use a list comprehension to encode the message
    encoded = [c.swapcase() if c.isalpha() else c for c in message]
    encoded = [vowel_map[c.lower()] if c.lower() in vowel_map else c for c in encoded]
    return ''.join(encoded)
