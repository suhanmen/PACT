def encode(message):
    encoded = ""
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
            if char.lower() in vowels:
                encoded += chr(ord(char) + 2)
            else:
                encoded += char
        else:
            encoded += char
    return encoded
