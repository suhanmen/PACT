def encode(message):
    vowels = "aeiouAEIOU"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
            if char in vowels:
                index = (alphabet.index(char) + 2) % 26
                result += alphabet[index]
        else:
            result += char
    return result
