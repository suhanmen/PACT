def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                result += chr(ord(letter) + 2)
            else:
                result += letter.swapcase()
        else:
            result += letter
    return result
