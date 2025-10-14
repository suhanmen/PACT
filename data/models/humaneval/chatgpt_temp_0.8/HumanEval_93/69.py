def encode(message):
    vowels = 'aeiouAEIOU'
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                # Find the index of the vowel and get the letter 2 places ahead
                index = ord(letter.lower()) - 97
                encoded += chr((index + 2) % 26 + 97)
            else:
                # Swap upper and lower case
                if letter.isupper():
                    encoded += letter.lower()
                else:
                    encoded += letter.upper()
        else:
            encoded += letter
    return encoded
