def encode(message):
    encoded_message = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_message += letter.upper()
            else:
                encoded_message += letter.lower()
            
            if letter.lower() in vowels:
                index = ord(letter.lower()) - ord('a')
                encoded_letter = chr((index + 2) % 26 + ord('a'))
                if letter.islower():
                    encoded_message = encoded_message[:-1] + encoded_letter
                else:
                    encoded_message = encoded_message[:-1] + encoded_letter.upper() 
        else:
            encoded_message += letter
            
    return encoded_message
