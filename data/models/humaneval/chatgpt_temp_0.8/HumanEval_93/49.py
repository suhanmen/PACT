def encode(message):
    vowels = "aeiouAEIOU"
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded_letter = chr(ord(letter)+2)
            else:
                encoded_letter = letter
            if letter.isupper():
                encoded_message += encoded_letter.lower()
            else:
                encoded_message += encoded_letter.upper()
        else:
            encoded_message += letter
    return encoded_message
