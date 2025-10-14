def encode(message):
    vowels = 'aeiouAEIOU'
    encoded = ''
    for letter in message:
        # Swap case of letters
        if letter.isalpha():
            if letter.islower():
                encoded += letter.upper()
            else:
                encoded += letter.lower()
        else:
            encoded += letter
        # Replace vowels
        if letter in vowels:
            new_letter = chr(ord(letter)+2)
            if new_letter in vowels:
                if letter.islower():
                    new_letter = chr(ord(new_letter)+2)
                else:
                    new_letter = chr(ord(new_letter)+2).upper()
            encoded = encoded[:-1] + new_letter
    return encoded
