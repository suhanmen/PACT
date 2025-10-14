def encode(message):
    vowels = "AEIOUaeiou"
    encoded = ""
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded += chr(ord(char)+2)
            else:
                if char.islower():
                    encoded += char.upper()
                else:
                    encoded += char.lower()
        else:
            encoded += char
    return encoded
