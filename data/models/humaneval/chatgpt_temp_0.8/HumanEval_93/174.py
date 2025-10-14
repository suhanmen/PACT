def encode(message):
    vowels = "aeiouAEIOU"
    encoded = ""
    for letter in message:
        if letter in vowels:
            encoded += chr(ord(letter) + 2)
        elif letter.islower():
            encoded += letter.upper()
        elif letter.isupper():
            encoded += letter.lower()
        else:
            encoded += letter
    return encoded
