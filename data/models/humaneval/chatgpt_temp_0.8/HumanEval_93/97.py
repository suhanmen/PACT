def encode(message):
    vowels = "AEIOUaeiou"
    result = ""
    for letter in message:
        if letter in vowels:
            # Replace vowel with letter 2 places ahead in alphabet
            encoded_letter = chr((ord(letter) + 2 - 65) % 26 + 65)
        else:
            # Swap case of non-vowel letters
            encoded_letter = letter.swapcase()
        result += encoded_letter
    return result
