def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for letter in message:
        if letter in vowels:
            index = ord(letter.lower()) - 97 # Get index of the vowel
            new_letter = chr((index + 2) % 26 + 97) # Get new letter
            result += new_letter.upper() if letter.isupper() else new_letter # Swap case
        elif letter.isalpha():
            result += letter.swapcase() # Swap case
        else:
            result += letter
    return result
