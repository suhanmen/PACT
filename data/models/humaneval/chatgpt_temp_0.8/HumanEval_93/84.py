def encode(message):
    """
    Encode a message by swapping letter cases and replacing vowels with letters 2 places ahead.

    Args:
    message (str): The message to encode

    Returns:
    str: The encoded message
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ""

    # Swap case of all letters and replace vowels with letters 2 places ahead
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded += chr(ord(char) + 2)
            else:
                encoded += char.swapcase()
        else:
            encoded += char

    return encoded
