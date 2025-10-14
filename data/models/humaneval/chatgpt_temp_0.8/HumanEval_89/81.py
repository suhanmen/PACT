def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alphabet[4:] + alphabet[:4]
    encrypted = ''
    for char in s:
        if char in alphabet:
            encrypted += shifted[alphabet.index(char)]
        else:
            encrypted += char
    return encrypted
