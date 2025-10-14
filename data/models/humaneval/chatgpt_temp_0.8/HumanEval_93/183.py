python
def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_char = char.upper()
            else:
                encoded_char = char.lower()
            if char.lower() in vowels:
                encoded_char = chr(ord(char) + 2)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message
