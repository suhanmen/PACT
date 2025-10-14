def encode(message):
    # create a dictionary to map vowels to their 2nd letter in the alphabet
    vowel_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    
    # initialize an empty string to store the encoded message
    encoded_message = ''
    
    # iterate over each character in the message
    for char in message:
        # check if the character is a vowel
        if char.lower() in vowel_map:
            # if it is a vowel, replace it with the corresponding letter 2 places ahead in the alphabet
            encoded_message += vowel_map[char.lower()]
        else:
            # if it is not a vowel, swap the case of the letter and add it to the encoded message
            if char.isupper():
                encoded_message += char.lower()
            else:
                encoded_message += char.upper()
    
    return encoded_message
