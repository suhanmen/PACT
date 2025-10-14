python
def encode(message):
    vowels = set('aeiouAEIOU')
    result = ''
    for char in message:
        if char.isalpha():
            # Swap case of letters
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
            # Replace vowels
            if char in vowels:
                result += chr(ord(char) + 2)
            else:
                result += char
        else:
            result += char
    return result
