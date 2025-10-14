def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for letter in s:
        index = alphabet.find(letter)
        shifted_index = (index + (2 * 2)) % 26
        encrypted += alphabet[shifted_index]
    return encrypted
