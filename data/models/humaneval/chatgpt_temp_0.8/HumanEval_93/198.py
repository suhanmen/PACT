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
    # Define the vowels and their replacements
    vowels = 'aeiou'
    vowel_replacements = {v: chr(ord(v) + 2) for v in vowels}
    
    # Create an empty string to store the encoded message
    encoded_message = ''
    
    # Iterate through each character in the message
    for char in message:
        # If the character is a letter, swap its case
        if char.isalpha():
            char = char.swapcase()
        
        # If the character is a vowel, replace it with the corresponding replacement
        if char.lower() in vowels:
            char = vowel_replacements[char.lower()]
        
        # Add the character to the encoded message
        encoded_message += char
    
    return encoded_message
