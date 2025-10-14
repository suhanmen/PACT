def encode(message):
    vowels = "aeiouAEIOU"
    encoded_msg = ""
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_char = chr(ord(char) + 2)
            else:
                encoded_char = char.swapcase()
            encoded_msg += encoded_char
        else:
            encoded_msg += char
    return encoded_msg
