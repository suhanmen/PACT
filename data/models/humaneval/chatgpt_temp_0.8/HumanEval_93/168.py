def encode(message):
    vowels = 'AEIOUaeiou'
    result = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_char = chr(ord(char) + 2)
            else:
                encoded_char = char
            if char.isupper():
                result += encoded_char.lower()
            else:
                result += encoded_char.upper()
        else:
            result += char
    return result
