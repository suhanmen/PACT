def encode(message):
    encoded = ""
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded += letter.upper()
            else:
                encoded += letter.lower()
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                encoded += chr(ord(letter)+2)
            else:
                encoded += letter
        else:
            encoded += letter
    return encoded
