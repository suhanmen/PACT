def encode(message):
    """
    Encode a message by swapping the case of all letters and replacing
    vowels with the letter that appears 2 places ahead of them in the 
    english alphabet.
    """
    # Create a dictionary to map vowels to their replacements
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    
    # Initialize an empty list to store the encoded characters
    encoded = []
    
    # Loop over each character in the message
    for char in message:
        # Swap the case of the character
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = char.lower()
        
        # Replace vowels with their 2nd alphabetically succeeding letters
        if char.lower() in vowels:
            char = vowels[char.lower()]
        
        # Append the encoded character to the list
        encoded.append(char)
    
    # Join the list of encoded characters into a string and return it
    return ''.join(encoded)
