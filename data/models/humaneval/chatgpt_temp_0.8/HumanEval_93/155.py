python
def encode(message):
    """
    Takes a message, and encodes in such a way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that vowel in the english alphabet. 
    Assume only letters. 
    """
    # create a dictionary to map vowels to their replacements
    vowel_dict = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    
    # create an empty list to store the encoded characters
    encoded = []
    
    # iterate through each character in the message
    for char in message:
        # if the character is a vowel, replace it according to the vowel_dict
        if char in vowel_dict:
            encoded.append(vowel_dict[char])
        # if the character is a letter, swap its case
        elif char.isalpha():
            if char.isupper():
                encoded.append(char.lower())
            else:
                encoded.append(char.upper())
        # 
