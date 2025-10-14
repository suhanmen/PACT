def encode(message):
    vowels = 'aeiou'
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                new_letter = chr(ord(letter)+2)
                if new_letter in vowels:
                    new_letter = new_letter.upper()
                encoded += new_letter
            else:
                if letter.isupper():
                    encoded += letter.lower()
                else:
                    encoded += letter.upper()
        else:
            encoded += letter
    return encoded
