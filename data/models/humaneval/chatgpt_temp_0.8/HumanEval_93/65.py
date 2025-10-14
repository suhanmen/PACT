python
def encode(message):
    result = ''
    vowels = 'aeiouAEIOU'
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                # If the letter is a vowel, replace it with the
                # letter 2 positions ahead in the alphabet
                new_letter = chr(ord(letter) + 2)
            else:
                # If the letter is a consonant, swap its case
                if letter.islower():
                    new_letter = letter.upper()
                else:
                    new_letter = letter.lower()
        else:
            # If the character is not a letter, leave it as is
            new_letter = letter
        result += new_letter
    return result
