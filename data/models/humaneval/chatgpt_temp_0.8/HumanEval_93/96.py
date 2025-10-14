def encode(message):
    vowels = 'aeiouAEIOU'
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                letter = chr(ord(letter)+2)
            else:
                if letter.islower():
                    letter = letter.upper()
                else:
                    letter = letter.lower()
        encoded += letter
    return encoded
