def encode(message):
    vowels = 'aeiou'
    output = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                output += chr(ord(letter) + 2)
            else:
                output += letter.swapcase()
        else:
            output += letter
    return output
