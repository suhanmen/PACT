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
    encoded_message = ""

    for letter in message:
        if letter in vowels:
            # Replace vowels with letter 2 places ahead
            if letter == 'u':
                encoded_message += 'W'
            elif letter == 'U':
                encoded_message += 'w'
            elif letter == 'o':
                encoded_message += 'Q'
            elif letter == 'O':
                encoded_message += 'q'
            elif letter == 'i':
                encoded_message += 'K'
            elif letter == 'I':
                encoded_message += 'k'
            elif letter == 'e':
                encoded_message += 'G'
            elif letter == 'E':
                encoded_message += 'g'
            elif letter == 'a':
                encoded_message += 'C'
            elif letter == 'A':
                encoded_message += 'c'
        else:
            # Swap case of letter
            if letter.isupper():
                encoded_message += letter.lowe
