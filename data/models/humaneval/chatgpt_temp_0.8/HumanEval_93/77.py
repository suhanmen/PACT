def encode(message):
    vowels = "AEIOUaeiou"
    encoded_message = ""
    
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                # Replace vowel with letter 2 positions ahead
                index = ord(letter) + 2
                if letter.isupper() and index > ord('Z'):
                    index -= 26
                elif letter.islower() and index > ord('z'):
                    index -= 26
                encoded_message += chr(index)
            else:
                # Swap case of letter
                encoded_message += letter.lower() if letter.isupper() else letter.upper()
        else:
            encoded_message += letter
    
    return encoded_message
