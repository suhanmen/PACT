def encode(message):
    vowels = "AEIOUaeiou"
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_char = chr(ord(char)+2)
                if new_char in vowels:
                    new_char = chr(ord(new_char)+2)
            else:
                if char.isupper():
                    new_char = char.lower()
                else:
                    new_char = char.upper()
        else:
            new_char = char
        encoded_message += new_char
    return encoded_message
