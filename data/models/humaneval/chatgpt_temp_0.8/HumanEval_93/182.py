def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char.isalpha():
            # Swap case of the letter
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            # Replace vowels with the letter 2 places ahead
            if char in vowels:
                char = chr(ord(char) + 2)
                if char > 'Z':
                    char = chr(ord(char) - 26)
        result += char
    return result
