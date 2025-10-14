def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    encoded = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
            if char.lower() in vowels:
                encoded += vowels[char.lower()].upper() if char.islower() else vowels[char.lower()]
        else:
            encoded += char
    return encoded
