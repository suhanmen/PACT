def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for letter in s:
        index = (alphabet.index(letter) + shift) % 26
        encrypted += alphabet[index]
    return encrypted
