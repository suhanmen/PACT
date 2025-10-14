def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_message += chr(ord(char)+2) #replace vowel with 2 letters ahead
            else:
                encoded_message += char.swapcase() #swap case of non-vowel letters
        else:
            encoded_message += char
    return encoded_message
