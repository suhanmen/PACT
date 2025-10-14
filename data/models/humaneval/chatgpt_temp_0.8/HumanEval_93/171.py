def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                # Replace the vowel with the letter 2 places ahead
                new_letter = chr(ord(letter) + 2)
            else:
                # Swap the case of the letter
                if letter.isupper():
                    new_letter = letter.lower()
                else:
                    new_letter = letter.upper()
            result += new_letter
        else:
            result += letter
    return result
