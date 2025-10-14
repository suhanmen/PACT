def encode(message):
    """
    Takes a message and encodes it by swapping the case of all letters and 
    replacing all vowels with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. Assumes only letters in the message.
    """
    vowels = 'aeiouAEIOU'
    encoded = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                # Replace vowels with letter 2 places ahead in the alphabet
                encoded += chr(ord(char) + 2).swapcase()
            else:
                # Swap the case of uppercase and lowercase letters
                encoded += char.swapcase()
        else:
            # Leave non-letter characters as they are
            encoded += char
    return encoded
