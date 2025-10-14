def encode(message):
    encoded = ''
    vowels = 'aeiouAEIOU'
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded += chr(ord(letter)+2)
            else:
                if letter.islower():
                    encoded += letter.upper()
                else:
                    encoded += letter.lower()
        else:
            encoded += letter
    return encoded
