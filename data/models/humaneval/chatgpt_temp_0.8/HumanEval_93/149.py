python
def encode(message):
    vowels = 'AEIOUaeiou'
    result = []
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                new_letter = chr((ord(letter) + 2 - 65) % 26 + 65)
            else:
                new_letter = letter.swapcase()
            result.append(new_letter)
        else:
            result.append(letter)
    return ''.join(result)
