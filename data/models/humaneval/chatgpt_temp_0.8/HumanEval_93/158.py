def encode(message):
    vowels = set('AEIOUaeiou')
    result = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                result += chr(ord(char) + 2)
            else:
                result += char.swapcase()
        else:
            result += char
    return result
