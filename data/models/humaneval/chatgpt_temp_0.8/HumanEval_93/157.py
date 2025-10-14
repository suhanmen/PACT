def encode(message):
    # Define a variable to store the encoded message
    encoded_message = ""
    
    # Loop through each character in the message
    for char in message:
        # If the character is a letter
        if char.isalpha():
            # Swap the case of the letter
            if char.isupper():
                encoded_char = char.lower()
            else:
                encoded_char = char.upper()
            
            # Replace vowels with the letter that appears 2 places ahead in the alphabet
            if encoded_char in "aeiou":
                encoded_char = chr(ord(encoded_char) + 2)
                if encoded_char > "z":
                    encoded_char = chr(ord(encoded_char) - 26)
        
        else:
            encoded_char = char
        
        # Add the encoded character to the encoded message
        encoded_message += encoded_char
    
    # Return the encoded message
    return encoded_message
