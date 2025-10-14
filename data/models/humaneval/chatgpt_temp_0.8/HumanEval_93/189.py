def encode(message):
    vowels = 'AEIOUaeiou'
    result = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                new_letter = chr((ord(letter) + 2 - 97) % 26 + 97)
                result += new_letter.upper() if new_letter.isupper() else new_letter.lower()
            else:
                result += letter.swapcase()
        else:
            result += letter
    return result
