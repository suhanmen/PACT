def encode(message):
    vowels = 'aeiouAEIOU'
    encrypted_message = ''
    for letter in message:
        if letter in vowels:
            encrypted_message += chr(ord(letter)+2)
        elif letter.islower():
            encrypted_message += letter.upper()
        elif letter.isupper():
            encrypted_message += letter.lower()
        else:
            encrypted_message += letter
    return encrypted_message
