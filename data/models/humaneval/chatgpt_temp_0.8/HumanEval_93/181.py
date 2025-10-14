def encode(message):
    vowels = 'aeiou'
    encoded = ''
    for letter in message:
        if letter.isalpha():
            # Swap case
            if letter.isupper():
                encoded += letter.lower()
            else:
                encoded += letter.upper()
            # Replace vowels
            if letter.lower() in vowels:
                new_letter = chr(ord(letter)+2)
                if new_letter in vowels:
                    new_letter = chr(ord(new_letter)+2)
                encoded = encoded[:-1] + new_letter
        else:
            encoded += letter
    return encoded
