def encode(message):
    vowels = "AEIOUaeiou"
    result = ""
    for char in message:
        if char.isalpha():
            if char in vowels:
                result += chr(ord(char)+2) # replace vowel with letter 2 positions ahead
            else:
                if char.isupper():
                    result += char.lower() # swap case of uppercase letters
                else:
                    result += char.upper() # swap case of lowercase letters
        else:
            result += char
    return result
