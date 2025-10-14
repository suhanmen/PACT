def encode(message):
    vowels = 'AEIOUaeiou'
    encoded = ''
    for char in message:
        # Swap case of all letters
        if char.isalpha():
            if char.isupper():
                encoded += char.lower()
            else:
                encoded += char.upper()
        # Replace all vowels
        elif char in vowels:
            index = ord(char) + 2
            if char.isupper():
                if index > ord('Z'):
                    index -= 26
                encoded += chr(index)
            else:
                if index > ord('z'):
                    index -= 26
                encoded += chr(index)
        # Keep non-letter characters the same
        else:
            encoded += char
    return encoded
