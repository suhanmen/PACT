def encode(message):
    vowels = "aeiouAEIOU"
    encoded_message = ""
    for letter in message:
        if letter in vowels:
            letter = chr(ord(letter)+2)  # shift the vowel 2 letters forward
        elif letter.isalpha():
            letter = letter.swapcase()  # swap case of non-vowel letters
        encoded_message += letter
    return encoded_message
