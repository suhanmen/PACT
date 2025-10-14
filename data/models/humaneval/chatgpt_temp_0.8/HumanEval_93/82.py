def encode(message):
    vowels = "aeiouAEIOU"
    encoded_message = ""
    for char in message:
        if char.isalpha():
            # Swap case of the letter
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            # Replace vowels with the letter 2 places ahead
            if char in vowels:
                encoded_message += chr(ord(char) + 2)
            else:
                encoded_message += char
        else:
            encoded_message += char
    return encoded_message
