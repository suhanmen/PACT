def encode(message):
    vowels = "AEIOUaeiou"
    encoded = ""
    for char in message:
        if char.isalpha():
            # Swap case of letters
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            # Replace vowels
            if char in vowels:
                char = chr(ord(char)+2)
                if char in vowels:
                    char = chr(ord(char)+2)
        encoded += char
    return encoded
