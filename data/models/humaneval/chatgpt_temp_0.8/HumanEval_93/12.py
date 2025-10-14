def encode(message):
    vowels = "aeiouAEIOU"
    encoded_message = ""
    for letter in message:
        if letter in vowels:
            letter = chr(ord(letter)+2)
        elif letter.isalpha():
            letter = letter.swapcase()
        encoded_message += letter
    return encoded_message
