def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:] + alphabet[:2] # Rotate the alphabet by shifting the letters down by 2*2 places
    result = ''
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            result += rotated_alphabet[index]
        else:
            result += char
    return result
