def encode(message):
    vowels = "AEIOUaeiou"
    encoded_message = ""
    for char in message:
        # Swap case of letters
        if char.isalpha():
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
        # Replace vowels with letter 2 places ahead in alphabet
        if char in vowels:
            char = chr(ord(char)+2)
            if char > 'Z' and char < 'a':
                char = chr(ord(char)-26)
            elif char > 'z':
                char = chr(ord(char)-26)
        encoded_message += char
    return encoded_message
