def encrypt(s):
    shift = 2 * 2 # shift down by two multiplied to two places
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypted = ''
    for char in s:
        if char in alphabet:
            encrypted += shifted_alphabet[alphabet.index(char)]
        else:
            encrypted += char
    return encrypted
