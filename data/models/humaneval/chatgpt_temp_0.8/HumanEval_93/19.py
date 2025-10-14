def encode(message):
    vowels = set('aeiouAEIOU')  # set of all vowels
    encoded = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                # replace vowels with letter 2 places ahead in the alphabet
                encoded += chr(ord(char) + 2) if chr(ord(char) + 2) not in vowels else chr(ord(char) + 3)
            else:
                # swap case of non-vowels
                encoded += char.swapcase()
        else:
            # keep non-letter characters as is
            encoded += char
    return encoded
