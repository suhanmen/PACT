def encode(message):
    vowels = 'aeiouAEIOU' # list of vowels to check for
    result = '' # initialize the encoded message
    for letter in message:
        if letter.isalpha(): # check if it's a letter
            # swap case of the letter
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
            # check if it's a vowel
            if letter in vowels:
                # replace it with the letter 2 places ahead in the alphabet
                letter = chr(ord(letter) + 2)
                if letter > 'z': # handle wrap-around for 'u' and 'U'
                    letter = chr(ord(letter) - 26)
            # add the letter to the result
            result += letter
        else: # add non-letter characters as-is
            result += letter
    return result
