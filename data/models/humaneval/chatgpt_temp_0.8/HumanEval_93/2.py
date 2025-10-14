def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char.isalpha():
            # Swap case of letter
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            
            # Replace vowel
            if char in vowels:
                char = chr(ord(char) + 2)
                if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                    char = char.upper()
        
        encoded_message += char
    
    return encoded_message
