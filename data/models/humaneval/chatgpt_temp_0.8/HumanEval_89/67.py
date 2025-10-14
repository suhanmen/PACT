def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[4:] + alphabet[:4]
    encrypted = ''
    for char in s:
        if char in alphabet:
            encrypted += shifted_alphabet[alphabet.index(char)]
        else:
            encrypted += char
    return encrypted
