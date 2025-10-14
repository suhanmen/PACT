def encode(message):
    vowels = "aeiouAEIOU"
    encoded = ""
    for letter in message:
        if letter.isalpha():
            # Swap case of the letter
            if letter.isupper():
                encoded += letter.lower()
            else:
                encoded += letter.upper()
            # Replace vowel with letter 2 places ahead in alphabet
            if letter in vowels:
                encoded = encoded[:-1] + chr(ord(letter) + 2)
        else:
            encoded += letter
    return encoded
