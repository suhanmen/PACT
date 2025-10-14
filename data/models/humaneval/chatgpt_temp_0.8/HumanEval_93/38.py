def encode(message):
    vowels = "AEIOUaeiou"
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                result += chr((ord(letter) + 2 - 65) % 26 + 65)
            else:
                if letter.isupper():
                    result += letter.lower()
                else:
                    result += letter.upper()
        else:
            result += letter
    return result
