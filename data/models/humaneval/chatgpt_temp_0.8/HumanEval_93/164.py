def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            # If the character is a vowel, replace it with the letter two places ahead in the alphabet
            result += chr(ord(char) + 2)
        else:
            # Swap the case of the character
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
    return result
