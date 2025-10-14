def encode(message):
    vowels = "AEIOUaeiou"
    result = ""
    for char in message:
        if char in vowels:
            # Replace the vowel with the letter 2 places ahead of it in the alphabet
            result += chr(ord(char) + 2)
        else:
            # Swap case of letter
            result += char.swapcase()
    return result
