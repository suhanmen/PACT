python
def encode(message):
    vowels = 'AEIOUaeiou'
    encoded = ''
    for char in message:
        if char in vowels:
            # If the character is a vowel, find the letter that appears 2 places ahead of it in the alphabet
            encoded += chr(ord(char) + 2)
        elif char.isalpha():
            # If the character is a letter, swap case
            if char.isupper():
                encoded += char.lower()
            else:
                encoded += char.upper()
        else:
            # For any other character, just append it to the encoded message
            encoded += char
    return encoded
