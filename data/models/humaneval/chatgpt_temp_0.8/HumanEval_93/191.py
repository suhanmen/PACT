def encode(message):
    vowels = 'AEIOUaeiou'
    result = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_char = chr(ord(char) + 2)
                if new_char in vowels:
                    new_char = chr(ord(new_char) + 2)
            else:
                new_char = char.swapcase()
            result += new_char
        else:
            result += char
    return result
