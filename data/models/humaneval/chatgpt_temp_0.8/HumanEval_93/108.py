def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_char = chr(ord(char) + 2)
            else:
                new_char = char.swapcase()
            result += new_char
        else:
            result += char
    return result
